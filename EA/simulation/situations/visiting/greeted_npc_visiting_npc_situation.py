from sims4.tuning.instances import lock_instance_tunables
class GreetedNPCVisitingNPCSituation(VisitingNPCSituation):
    INSTANCE_TUNABLES = {'greeted_npc_sims': sims4.tuning.tunable.TunableTuple(situation_job=situations.situation_job.SituationJob.TunableReference(description='\n                    The job given to NPC sims in the visiting situation.\n                    '), role_state=role.role_state.RoleState.TunableReference(description='\n                    The role state given to NPC sims in the visiting situation.\n                    '), tuning_group=GroupNames.ROLES)}

    @classmethod
    def _states(cls):
        return (SituationStateData(1, GreetedNPCVisitingNPCState),)

    @classmethod
    def _get_tuned_job_and_default_role_state_tuples(cls):
        return [(cls.greeted_npc_sims.situation_job, cls.greeted_npc_sims.role_state)]

    @classmethod
    def default_job(cls):
        return cls.greeted_npc_sims.situation_job

    def start_situation(self):
        super().start_situation()
        self._change_state(GreetedNPCVisitingNPCState())

class GreetedNPCVisitingNPCState(situations.situation_complex.SituationState):
    pass
