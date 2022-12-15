from __future__ import annotations

import logging

from src.declare4py.process_models.decl_model import DeclModel
from src.declare4py.pm_tasks.log_generation.asp.asp_generator import AspGenerator

logging.basicConfig(level=logging.DEBUG)



decl2 = """
activity Driving_Test
bind Driving_Test: Driver, Grade
activity Getting_License
bind Getting_License: Driver
activity Resit
bind Resit: Driver, Grade
activity Test_Failed
bind Test_Failed: Driver
Driver: Fabrizio, Mike, Marlon, Raimundas
Grade: integer between 1 and 5
# Response[Driving_Test, Getting_License] |A.Grade>2 | |
Response[Driving_Test, Getting_License] | |T.Grade>2 |
Response[Driving_Test, Resit] |A.Grade<=2 | |
Response[Driving_Test, Test_Failed] |A.Grade<=2 | |
"""


decl = """activity ER_Triage
bind ER_Triage: org_group, Diagnose, Age
activity er_registration
bind er_registration: InfectionSuspected, org_group, DiagnosticBlood, DisfuncOrg, SIRSCritTachypnea, Hypotensie, SIRSCritHeartRate, Infusion, DiagnosticArtAstrup, Age, DiagnosticIC, DiagnosticSputum, DiagnosticLiquor, DiagnosticOther, SIRSCriteria2OrMore, DiagnosticXthorax, SIRSCritTemperature, DiagnosticUrinaryCulture, SIRSCritLeucos, Oligurie, DiagnosticLacticAcid, Diagnose, Hypoxie, DiagnosticUrinarySediment, DiagnosticECG
activity ER_Sepsis_Triage
bind ER_Sepsis_Triage: org_group, Diagnose, Age
activity Leucocytes
bind Leucocytes: Leucocytes, org_group, Diagnose, Age
activity CRP
bind CRP: CRP, org_group, Diagnose, Age
activity LacticAcid
bind LacticAcid: org_group, LacticAcid
activity iv_antibiotics
bind iv_antibiotics: org_group
activity admission_nc
bind admission_nc: org_group
activity iv_liquid
bind iv_liquid: org_group, Diagnose, Age
activity Release_A
bind Release_A: org_group
activity Return_ER
bind Return_ER: org_group
activity admission_ic
bind admission_ic: org_group
CRP: float between 5.87 and 573.78
InfectionSuspected: true, false
org_group: A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, QUESTION
DiagnosticBlood: true, false
DisfuncOrg: true, false
SIRSCritTachypnea: true, false
Hypotensie: true, false
SIRSCritHeartRate: true, false
Infusion: true, false
Leucocytes: float between 0.2 and 381.3
DiagnosticArtAstrup: true, false
LacticAcid: float between 0.2 and 14.9
Age: integer between 20 and 90
DiagnosticIC: true, false
DiagnosticSputum: false, true
DiagnosticLiquor: false, true
DiagnosticOther: false, true
SIRSCriteria2OrMore: true, false
DiagnosticXthorax: true, false
SIRSCritTemperature: true, false
DiagnosticUrinaryCulture: true, false
SIRSCritLeucos: false, true
Oligurie: false, true
DiagnosticLacticAcid: true, false
Diagnose: YA, YB, YC, YD, QA, QB, QC, QD, QE, IA, IB, IC, ID, IE, AA, AB, AC, AD, AE, ZA, ZB, ZC, ZD, RA, RB, RC, RD, JA, JB, JC, JD, JE, BA, BB, A, BC, B, BD, C, BE, D, E, F, G, H, I, J, K, L, M, N, SA, O, SB, P, SC, Q, SD, R, S, T, U, V, KA, W, KB, X, KC, Y, KD, Z, KE, CA, CB, CC, CD, CE, TA, TB, TC, TD, LA, LB, LC, LD, LE, DA, DB, DC, DD, DE, UA, UB, UC, UD, MA, MB, MC, MD, ME, EA, EB, EC, ED, EE, VA, VB, VC, VD, NA, NB, NC, ND, FA, FB, FC, FD, FE, WA, WB, WC, WD, OA, OB, OC, OD, OE, GA, GB, GC, GD, GE, XA, XB, XC, XD, PA, PB, PC, PD, PE, HA, HB, HC, HD, HE
Hypoxie: false, true
DiagnosticUrinarySediment: true, false
DiagnosticECG: true, false
Chain Response[admission_nc, Release_B] | A.org_group is K |T.org_group is E |
Chain Response[admission_nc, Release_A] | A.org_group is I |T.org_group is E | 133020,957701,s
Chain Precedence[iv_liquid, admission_nc] | A.org_group is I |T.org_group is A | 92,14473,s
#Chain Response[er_registration, ER_Triage] | (A.DiagnosticArtAstrup is false) AND (A.SIRSCritHeartRate is true) AND (A.org_group is A) AND (A.DiagnosticBlood is true) AND (A.DisfuncOrg is false) AND (A.DiagnosticECG is true) AND (A.Age >= 45) AND (A.InfectionSuspected is true) AND (A.DiagnosticLacticAcid is true) AND (A.DiagnosticSputum is true) AND (A.Hypoxie is false) AND (A.DiagnosticUrinaryCulture is true) AND (A.DiagnosticLiquor is false) AND (A.SIRSCritTemperature is true) AND (A.Infusion is true) AND (A.Hypotensie is false) AND (A.DiagnosticUrinarySediment is true) AND (A.Oligurie is false) AND (A.Age <= 80) AND (A.SIRSCritTachypnea is true) AND (A.DiagnosticOther is false) AND (A.SIRSCritLeucos is false) AND (A.DiagnosticIC is true) AND (A.SIRSCriteria2OrMore is true) AND (A.DiagnosticXthorax is true) | T.org_group is C |52,2154,s
Chain Response[er_registration, ER_Triage] | (A.DiagnosticArtAstrup is false) AND (A.SIRSCritHeartRate is true) AND (A.org_group is A) AND (A.DiagnosticBlood is true) | T.org_group is C |52,2154,s
Chain Precedence[Release_A, Return_ER] |A.org_group is QUESTION |T.org_group is E | 1121801,1121801,s
Chain Precedence[ER_Sepsis_Triage, iv_antibiotics] | A.org_group is L | T.org_group is L | 15,11000,s
Chain Response[ER_Sepsis_Triage, iv_antibiotics] | A.org_group is L | T.org_group is L | 15,11000,s
Chain Precedence[admission_ic, admission_nc] | A.org_group is J | T.org_group is J |
Chain Precedence[iv_antibiotics, admission_nc] | A.org_group is F | T.org_group is A | 92,14459,s
Chain Precedence[admission_nc, Release_B] | A.org_group is E | T.org_group is K | 48225,48225,s
Chain Response[admission_ic, admission_nc] | A.org_group is J | T.org_group is J | 61534,61534,s
Chain Response[LacticAcid, Leucocytes] | A.LacticAcid <= 0.8 | T.Leucocytes >= 13.8 | 0,2778,m
Chain Precedence[er_registration, ER_Triage] | A.org_group is C |(T.InfectionSuspected is true) AND (T.SIRSCritTemperature is true) AND (T.DiagnosticLacticAcid is true) AND (T.DiagnosticBlood is true) AND (T.DiagnosticIC is true) AND (T.SIRSCriteria2OrMore is true) AND (T.DiagnosticECG is true) |52,2154,s"""


decl = """activity ER Triage
bind ER Triage: org:group, Diagnose, Age
activity ER Registration
bind ER Registration: InfectionSuspected, org:group, DiagnosticBlood, DisfuncOrg, SIRSCritTachypnea, Hypotensie, SIRSCritHeartRate, Infusion, DiagnosticArtAstrup, Age, DiagnosticIC, DiagnosticSputum, DiagnosticLiquor, DiagnosticOther, SIRSCriteria2OrMore, DiagnosticXthorax, SIRSCritTemperature, DiagnosticUrinaryCulture, SIRSCritLeucos, Oligurie, DiagnosticLacticAcid, Diagnose, Hypoxie, DiagnosticUrinarySediment, DiagnosticECG
activity ER Sepsis Triage
bind ER Sepsis Triage: org:group, Diagnose, Age
activity Leucocytes
bind Leucocytes: Leucocytes, org:group, Diagnose, Age
activity CRP
bind CRP: CRP, org:group, Diagnose, Age
activity LacticAcid
bind LacticAcid: org:group, LacticAcid
activity IV Antibiotics
bind IV Antibiotics: org:group
activity Admission NC
bind Admission NC: org:group
activity IV Liquid
bind IV Liquid: org:group, Diagnose, Age
activity Release A
bind Release A: org:group
activity Return ER
bind Return ER: org:group
activity Admission IC
bind Admission IC: org:group
CRP: float between 5.78 and 573.74
InfectionSuspected: true, false
org:group: A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, ?
DiagnosticBlood: true, false
DisfuncOrg: true, false
SIRSCritTachypnea: true, false
Hypotensie: true, false
SIRSCritHeartRate: true, false
Infusion: true, false
Leucocytes: float between 0.2 and 381.3
DiagnosticArtAstrup: true, false
LacticAcid: float between 0.2 and 14.9
Age: integer between 20 and 90
DiagnosticIC: true, false
DiagnosticSputum: false, true
DiagnosticLiquor: false, true
DiagnosticOther: false, true
SIRSCriteria2OrMore: true, false
DiagnosticXthorax: true, false
SIRSCritTemperature: true, false
DiagnosticUrinaryCulture: true, false
SIRSCritLeucos: false, true
Oligurie: false, true
DiagnosticLacticAcid: true, false
Diagnose: YA, YB, YC, YD, QA, QB, QC, QD, QE, IA, IB, IC, ID, IE, AA, AB, AC, AD, AE, ZA, ZB, ZC, ZD, RA, RB, RC, RD, JA, JB, JC, JD, JE, BA, BB, A, BC, B, BD, C, BE, D, E, F, G, H, I, J, K, L, M, N, SA, O, SB, P, SC, Q, SD, R, S, T, U, V, KA, W, KB, X, KC, Y, KD, Z, KE, CA, CB, CC, CD, CE, TA, TB, TC, TD, LA, LB, LC, LD, LE, DA, DB, DC, DD, DE, UA, UB, UC, UD, MA, MB, MC, MD, ME, EA, EB, EC, ED, EE, VA, VB, VC, VD, NA, NB, NC, ND, FA, FB, FC, FD, FE, WA, WB, WC, WD, OA, OB, OC, OD, OE, GA, GB, GC, GD, GE, XA, XB, XC, XD, PA, PB, PC, PD, PE, HA, HB, HC, HD, HE
Hypoxie: false, true
DiagnosticUrinarySediment: true, false
DiagnosticECG: true, false
Chain Response[Admission NC, Release B] |A.org:group is K |T.org:group is E |
Chain Response[Admission NC, Release A] |A.org:group is I |T.org:group is E |133020,957701,s
Chain Precedence[IV Liquid, Admission NC] |A.org:group is I |T.org:group is A |92,14473,s
Chain Response[ER Registration, ER Triage] |(A.DiagnosticArtAstrup is false) AND (A.SIRSCritHeartRate is true) AND (A.org:group is A) AND (A.DiagnosticBlood is true) AND (A.DisfuncOrg is false) AND (A.DiagnosticECG is true) AND (A.Age >= 45) AND (A.InfectionSuspected is true) AND (A.DiagnosticLacticAcid is true) AND (A.DiagnosticSputum is true) AND (A.Hypoxie is false) AND (A.DiagnosticUrinaryCulture is true) AND (A.DiagnosticLiquor is false) AND (A.SIRSCritTemperature is true) AND (A.Infusion is true) AND (A.Hypotensie is false) AND (A.DiagnosticUrinarySediment is true) AND (A.Oligurie is false) AND (A.Age <= 80) AND (A.SIRSCritTachypnea is true) AND (A.DiagnosticOther is false) AND (A.SIRSCritLeucos is false) AND (A.DiagnosticIC is true) AND (A.SIRSCriteria2OrMore is true) AND (A.DiagnosticXthorax is true) |T.org:group is C |52,2154,s
Chain Precedence[Release A, Return ER] |A.org:group is ? |T.org:group is E |1121801,1121801,s
Chain Precedence[ER Sepsis Triage, IV Antibiotics] |A.org:group is L |T.org:group is L |15,11000,s
Chain Response[ER Sepsis Triage, IV Antibiotics] |A.org:group is L |T.org:group is L |15,11000,s
Chain Precedence[Admission IC, Admission NC] |A.org:group is J |T.org:group is J |
Chain Precedence[IV Antibiotics, Admission NC] |A.org:group is F |T.org:group is A |92,14459,s
Chain Precedence[Admission NC, Release B] |A.org:group is E |T.org:group is K |48225,48225,s
Chain Response[Admission IC, Admission NC] |A.org:group is J |T.org:group is J |61534,61534,s
Chain Response[LacticAcid, Leucocytes] |A.LacticAcid <= 0.8 |T.Leucocytes >= 13.8 |0,2778,m
Chain Precedence[ER Registration, ER Triage] |A.org:group is C |(T.InfectionSuspected is true) AND (T.SIRSCritTemperature is true) AND (T.DiagnosticLacticAcid is true) AND (T.DiagnosticBlood is true) AND (T.DiagnosticIC is true) AND (T.SIRSCriteria2OrMore is true) AND (T.DiagnosticECG is true) |52,2154,s
"""

decl = """
activity act1
activity act2
activity act3
activity act4
Existence[act1] | |
Existence[act2] | |
Existence[act3] | |
Existence[act4] | |
"""


# dp = DeclareParser()
# model = dp.parse_from_string(decl)
# dp = DeclModel().parse_from_file("...")

model: DeclModel = DeclModel().parse_from_string(decl)
model.violate_all_constraints_in_subset = True
model.add_constraints_subset_to_violate([
    # "Existence[act2] | |",
    # "Existence[act4] | |"
# "Chain Response[Admission IC, Admission NC] |A.org:group is J |T.org:group is J |61534,61534,s",
# "Chain Response[LacticAcid, Leucocytes] |A.LacticAcid <= 0.8 |T.Leucocytes >= 13.8 |0,2778,m",
])



num_of_traces = 4
num_min_events = 2
num_max_events = 4
asp = AspGenerator(
    model,
    num_of_traces,
    num_min_events,
    num_max_events,
    # distributor_type="gaussian",
    # loc=3, scale=0.8,
    encode_decl_model=False
)

asp.run()
asp.to_xes("../../generated_xes.xes")


# TODO: ask how to implement TIME CONDITION in asp
# TODO: Ask Chiarello whether the generated output of lp is correct


