from app.data_models import Payload, Project
from app.generators import TruffleShuffle


def get_team_name(project: Project) -> str:
    product_name = project.product
    team_code = project.teamCode
    return f"{product_name} - {team_code}"


def hat_trick(payload: Payload) -> Payload:
    random_project = TruffleShuffle(range(len(payload.projects)))
    placed_learners = []
    placed_learners.extend(map(lambda p: p.teamMemberSmtIds, payload.projects))

    for learner in payload.learners:

        if learner.labsProject != "":
            # project_assignment = learner.labsProject
            # project, *_ = filter(
            #     lambda p: get_team_name(p) == project_assignment,
            #     payload.projects,
            # )
            # if learner.lambdaId not in project.teamMemberSmtIds:
            #     print("Missing Learner!")
            #     print(f"Added {learner.name} to {project.product}")
            #     project.teamMemberSmtIds.append(learner.lambdaId)
            continue

        if learner.track == "Web":
            small = min(len(project.teamMemberSmtIds) for project in payload.projects)
            for project in payload.projects:
                if len(project.teamMemberSmtIds) == small:
                    project.teamMemberSmtIds.append(learner.lambdaId)
                    learner.labsProject = get_team_name(project)
                    break

        project_id = random_project()
        while learner.track not in payload.projects[project_id].tracks:
            project_id = random_project()

        payload.projects[project_id].teamMemberSmtIds.append(learner.lambdaId)
        learner.labsProject = get_team_name(payload.projects[project_id])

    return payload
