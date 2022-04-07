from app.data_models import Payload
from app.generators import TruffleShuffle


def hat_trick(payload: Payload) -> Payload:
    random_project = TruffleShuffle(range(len(payload.projects)))
    placed_learners = []
    placed_learners.extend(map(lambda p: p.teamMemberSmtIds, payload.projects))

    for learner in payload.learners:
        # Can it be the case that one is set but the other is not?!
        if learner.lambdaId in placed_learners and learner.labsProject != "":
            continue

        project_id = random_project()
        while learner.track not in payload.projects[project_id].tracks:
            project_id = random_project()

        product_name = payload.projects[project_id].product
        team_code = payload.projects[project_id].teamCode
        payload.projects[project_id].teamMemberSmtIds.append(learner.lambdaId)
        team_name = f"{product_name} - {team_code}"
        learner.labsProject = team_name
    return payload
