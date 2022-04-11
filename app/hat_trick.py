from app.data_models import Payload, Project
from app.generators import TruffleShuffle


def get_team_name(project: Project) -> str:
    product_name = project.product
    team_code = project.teamCode
    return f"{product_name} - {team_code}"


def hat_trick(payload: Payload) -> Payload:
    random_project = TruffleShuffle(range(len(payload.projects)))

    for learner in payload.learners:

        if learner.labsProject != "":
            continue

        project_id = random_project()
        while learner.track not in payload.projects[project_id].tracks:
            project_id = random_project()

        payload.projects[project_id].teamMemberSmtIds.append(learner.lambdaId)
        learner.labsProject = get_team_name(payload.projects[project_id])

    return payload
