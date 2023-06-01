from __future__ import annotations

import multiprocessing
from pm4py.objects.log.obj import Trace
from pythomata.impl.symbolic import SymbolicDFA

from src.Declare4Py.D4PyEventLog import D4PyEventLog
from src.Declare4Py.ProcessMiningTasks.AbstractConformanceChecking import AbstractConformanceChecking
from src.Declare4Py.ProcessModels.LTLModel import LTLModel
from src.Declare4Py.Utils.utils import Utils
from logaut import ltl2dfa
from functools import reduce
import pandas

"""
Provides basic conformance checking functionalities
"""


class LTLAnalyzer(AbstractConformanceChecking):

    def __init__(self, log: D4PyEventLog, ltl_model: LTLModel):
        super().__init__(log, ltl_model)

    @staticmethod
    def run_single_trace(trace: Trace, dfa: SymbolicDFA, activity_key: str = 'concept:name'):
        current_states = {dfa.initial_state}

        for event in trace:
            event = event[activity_key]
            symbol = Utils.parse_activity(event)
            symbol = symbol.lower()
            temp = dict()
            temp[symbol] = True

            current_states = reduce(
                set.union,
                map(lambda x: dfa.get_successors(x, temp), current_states),
                set(),
            )

        is_accepted = any(dfa.is_accepting(state) for state in current_states)
        return is_accepted

    @staticmethod
    def run_single_trace_par(args):
        trace, dfa, activity_key = args
        current_states = {dfa.initial_state}

        for event in trace:
            event = event[activity_key]
            symbol = Utils.parse_activity(event)
            symbol = symbol.lower()
            temp = dict()
            temp[symbol] = True

            current_states = reduce(
                set.union,
                map(lambda x: dfa.get_successors(x, temp), current_states),
                set(),
            )

        is_accepted = any(dfa.is_accepting(state) for state in current_states)
        return trace.attributes['concept:name'], is_accepted

    def run(self) -> pandas.DataFrame:
        """
        Performs conformance checking for the provided event log and an input LTL model.

        Returns:
            A pandas Dataframe containing the id of the traces and the result of the conformance check
        """

        if self.event_log is None:
            raise RuntimeError("You must load the log before checking the model.")
        if self.process_model is None:
            raise RuntimeError("You must load the LTL model before checking the model.")
        dfa = ltl2dfa(self.process_model.parsed_formula, backend="lydia") #lydia
        dfa = dfa.minimize()
        g_log = self.event_log.get_log()
        activity_key = self.event_log.activity_key

        results = []

        for trace in g_log:
            is_accepted = self.run_single_trace(trace, dfa, activity_key)
            results.append([trace.attributes[self.event_log.activity_key], is_accepted])

        return pandas.DataFrame(results, columns=[self.event_log.case_id_key, "accepted"])

    def run_par(self):
        dfa = ltl2dfa(self.process_model.parsed_formula, backend="lydia")  # lydia
        dfa = dfa.minimize()
        g_log = self.event_log.get_log()
        traces = g_log._list
        act_key = self.event_log.activity_key

        with multiprocessing.Pool(processes=4) as pool:
            results = pool.map(self.run_single_trace_par, zip(traces, [dfa] * len(traces),
                                                                           [act_key] * len(traces)))

        pandas.DataFrame(results, columns=[self.event_log.case_id_key, "accepted"])

    def run_aggregate(self) -> pandas.DataFrame:
        """
        Performs conformance checking for the provided event log and an input LTL model.

        Returns:
            A pandas Dataframe containing the id of the traces and the result of the conformance check
        """

        if self.event_log is None:
            raise RuntimeError("You must load the log before checking the model.")
        if self.process_model is None:
            raise RuntimeError("You must load the LTL model before checking the model.")
        dfa = ltl2dfa(self.process_model.parsed_formula, backend="lydia")
        dfa = dfa.minimize()
        group = self.event_log.groupby(self.event_log.case_id_key, as_index=True)
        results = group[self.event_log.activity_key].aggregate(self.run_single_trace, dfa=dfa, engine='cython')

        return pandas.DataFrame(results, columns=[self.event_log.case_id_key, "accepted"])
