from typing import List

from app.data_models import Payload, Project, Learner


def place(learner: Learner, projects: List[Project]):
    project = min(
        filter(lambda team: learner.track in team.tracks, projects),
        key=lambda team: len(team.teamMemberSmtIds),
    )
    project.teamMemberSmtIds.append(learner.lambdaId)
    learner.labsProject = project.id


def sorting_hat(payload: Payload) -> Payload:
    learners = sorted(payload.learners, key=lambda dev: dev.track)
    projects = sorted(
        payload.projects,
        key=lambda project: (-len(project.tracks), project.tracks),
        reverse=True,
    )
    for learner in learners:
        place(learner, projects)
    return payload
