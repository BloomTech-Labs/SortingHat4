from itertools import count
from typing import List, Iterable
from string import ascii_uppercase

from app.data_models import Payload, Project, Learner


def place(learner: Learner, projects: List[Project]):
    track_projects = filter(lambda team: learner.track in team.tracks, projects)
    target = min(track_projects, key=lambda team: len(team.teamMemberSmtIds))

    # if len(target.teamMemberSmtIds) >= 12:
    #     target = make_new_team(target, projects)

    target.teamMemberSmtIds.append(learner.lambdaId)
    learner.labsProject = target.id


def sorting_hat(payload: Payload) -> Payload:
    learners = sorted(payload.learners, key=lambda dev: dev.track)
    projects = sorted(
        payload.projects,
        key=lambda project: (-len(project.tracks), project.tracks),
        reverse=True,
    )
    for learner in learners:
        if not learner.labsProject:
            place(learner, projects)
    # projects = remove_empty_teams(projects)
    return Payload(learners=learners, projects=projects)


def next_team_code(current_codes: Iterable) -> str:

    def team_code_gen():
        counter = count(1)
        while True:
            groups = zip(*[ascii_uppercase] * next(counter))
            yield from ("".join(group) for group in groups)

    team_codes = team_code_gen()
    code = next(team_codes)
    while code in current_codes:
        code = next(team_codes)
    return code


def make_new_team(target: Project, projects: List[Project]):
    product = target.product
    current_codes = (team.teamCode for team in projects if team.product == product)
    team_code = next_team_code(current_codes)
    new_team = Project(
        id=f"{product} - {team_code}",
        product=product,
        teamCode=team_code,
        releaseManager=target.releaseManager,
        tracks=target.tracks,
        teamMemberSmtIds=[],
    )
    projects.append(new_team)
    return new_team


def remove_empty_teams(projects: List[Project]):
    return [project for project in projects if project.teamMemberSmtIds]
