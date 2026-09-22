#!/usr/bin/env python3
from dataclasses import dataclass, field

TERMINAL={"PASS","PARTIAL","FAIL","BLOCKED"}

@dataclass
class Case:
    state:str="START"
    history:list=field(default_factory=list)
    ground_truth_version:int=1
    old_scores_valid:bool=True
    validation_independent:bool=True
    last_accepted_builder:str="B0"

    def go(self,s,why):
        self.state=s; self.history.append((s,why))

def run(case_id):
    c=Case()
    c.go("WHOLE_PAPER_SCANNED","whole-paper gate")

    if case_id=="CL01":
        c.go("REFERENCE_CLOSED","later chapter recovered parameter")
        c.go("PASS","parameter not misclassified as calibratable")
    elif case_id=="CL02":
        c.go("REFERENCE_CLOSURE_OPEN","paper cites source")
        c.go("REFERENCE_CLOSED","lineage exhausted")
        c.go("BLOCKED","claim-critical target-specific item unresolved; no M2 approved")
    elif case_id=="CL03":
        c.go("SOURCE_CONFLICT","contradictory evidence preserved")
        c.go("PARTIAL","faithful variants retained; no silent correction")
    elif case_id=="CL04":
        c.go("MODEL_DEPENDENCY_FROZEN","upstream/downstream known")
        c.go("UPSTREAM_REOPENED","downstream tuning rejected")
        c.go("BLOCKED","upstream anchor still open")
    elif case_id=="CL05":
        c.go("GROUND_TRUTH_FROZEN","v1")
        c.ground_truth_version+=1; c.old_scores_valid=False
        c.go("G11_REOPENED","target corrected; old scores invalidated")
        c.go("PASS","recomputed on v2")
    elif case_id=="CL06":
        c.go("STOP_TUNING","two repairs <10%")
        c.go("EVIDENCE_REVIEW","no more blind calibration")
        c.go("BLOCKED","evidence exhausted, no defensible M2")
    elif case_id=="CL07":
        c.go("VALIDATOR_RUNNING","candidate B1")
        c.go("ROLLBACK","frozen anchor regression damaged")
        assert c.last_accepted_builder=="B0"
        c.go("PARTIAL","B0 retained")
    elif case_id=="CL08":
        c.go("BUILDER_FROZEN","holdout untouched")
        c.go("VALIDATOR_RUNNING","detailed residual exposed")
        c.validation_independent=False
        c.go("EXPOSED_DEVELOPMENT_EVIDENCE","builder used residual")
        c.go("PARTIAL","cannot claim independent validation")
    elif case_id=="CL09":
        c.go("STOP_TUNING","numerical knob used for fit")
        c.go("EVIDENCE_REVIEW","numerical settings restored to convergence role")
        c.go("BLOCKED","no physical/evidence repair yet")
    elif case_id=="CL10":
        c.go("BUILDER_FROZEN","handoff")
        c.go("VALIDATOR_RUNNING","validator tries parameter/tolerance mutation")
        c.go("ROLE_VIOLATION","mutation rejected")
        c.go("BLOCKED","fresh frozen handoff required")
    elif case_id=="CL11":
        c.go("GROUND_TRUTH_FROZEN","borrowed data tagged with original source/protocol")
        c.go("PASS","provenance preserved")
    elif case_id=="CL12":
        c.go("STOP_TUNING","persistent structured residual")
        c.go("EVIDENCE_REVIEW","whole-paper/reference/model/units/algorithm review")
        c.go("BLOCKED","TERMINAL_BLOCKED; no silent return to tuning")
    elif case_id=="CL13":
        c.go("VALIDATOR_RUNNING","good-looking result but source/provenance component missing")
        c.go("VALIDATION_PACKET_INCOMPLETE","formal PASS/PARTIAL forbidden")
        c.go("BLOCKED","complete source/fresh-run/metrics/verdict packet first")
    elif case_id=="CL14":
        c.go("VALIDATOR_RUNNING","metric family does not test the paper claim")
        c.go("METRIC_ROUTING_REJECTED","replace waveform/pixel metric with typed frequency/topology metrics")
        c.go("BLOCKED","typed metric family required before verdict")
    else:
        raise KeyError(case_id)
    assert c.state in TERMINAL
    return c

if __name__=="__main__":
    for i in range(1,15):
        cid=f"CL{i:02d}"
        c=run(cid)
        print(cid,c.state," -> ".join(s for s,_ in c.history))
