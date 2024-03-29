from typing import List

from numpy.random import randint

from app.data_models import Payload, Learner, Project
from app.generators import random_uuid, random_name


def random_learner(track: str):
    return Learner(
        oktaId=random_uuid(),
        name=random_name(),
        track=track,
        tpmSkill1="B",
        tpmSkill2="B",
        tpmSkill3="C",
        tpmInterest1=randint(1, 4),
        tpmInterest2=randint(1, 4),
        tpmInterest3=randint(1, 4),
        tpmInterest4=randint(1, 4),
        uxInterest1=randint(1, 4),
        uxInterest2=randint(1, 4),
        frontendInterest1=randint(1, 4),
        frontendInterest2=randint(1, 4),
        backendInterest1=randint(1, 4),
        backendInterest2=randint(1, 4),
    )


def random_returning_learner(track: str, labs_project: str):
    return Learner(
        oktaId=random_uuid(),
        name=random_name(),
        track=track,
        storyPoints=randint(1, 21),
        labsProject=labs_project,
        tpmSkill1="B",
        tpmSkill2="B",
        tpmSkill3="C",
        tpmInterest1=randint(1, 4),
        tpmInterest2=randint(1, 4),
        tpmInterest3=randint(1, 4),
        tpmInterest4=randint(1, 4),
        uxInterest1=randint(1, 4),
        uxInterest2=randint(1, 4),
        frontendInterest1=randint(1, 4),
        frontendInterest2=randint(1, 4),
        backendInterest1=randint(1, 4),
        backendInterest2=randint(1, 4),
    )


def random_project(product: str,
                   team_code: str,
                   tracks: List[str],
                   members: List[str]):
    return Project(
        id=f"{product} - {team_code}",
        product=product,
        teamCode=team_code,
        releaseManager=random_name(),
        tracks=tracks,
        teamMemberSmtIds=members,
    )


def example_payload():
    learners = [
        random_learner("Web"),
        random_learner("Web"),
        random_learner("Web"),
        random_learner("Web"),
        random_learner("Data Science"),
        random_learner("Data Science"),
        random_learner("Backend"),
        random_learner("Backend"),
        random_returning_learner("Web", "Test Product - A"),
        random_returning_learner("Web", "Test Product - A"),
        random_returning_learner("Web", "Test Product - A"),
        random_returning_learner("Web", "Test Product - A"),
        random_returning_learner("Data Science", "Test Product - A"),
        random_returning_learner("Data Science", "Test Product - A"),
        random_returning_learner("Backend", "Test Product - B"),
        random_returning_learner("Backend", "Test Product - B"),
        random_returning_learner("Web", "Test Product - B"),
        random_returning_learner("Web", "Test Product - B"),
        random_returning_learner("Web", "Test Product - B"),
        random_returning_learner("Web", "Test Product - B"),
        random_returning_learner("Web", "Test Product - C"),
        random_returning_learner("Web", "Test Product - C"),
        random_returning_learner("Web", "Test Product - C"),
        random_returning_learner("Web", "Test Product - C"),
        random_returning_learner("Data Science", "Test Product - C"),
        random_returning_learner("Data Science", "Test Product - C"),
        random_returning_learner("Backend", "Test Product - D"),
        random_returning_learner("Backend", "Test Product - D"),
        random_returning_learner("Web", "Test Product - D"),
        random_returning_learner("Web", "Test Product - D"),
        random_returning_learner("Web", "Test Product - D"),
        random_returning_learner("Web", "Test Product - D"),
    ]
    projects = [
        random_project("Test Product", "A", ["Web", "Data Science"], [
           learner.oktaId for learner in learners
           if "Test Product - A" == learner.labsProject
        ]),
        random_project("Test Product", "B", ["Web", "Backend"], [
           learner.oktaId for learner in learners
           if "Test Product - B" == learner.labsProject
        ]),
        random_project("Test Product", "C", ["Web", "Backend"], [
            learner.oktaId for learner in learners
            if "Test Product - C" == learner.labsProject
        ]),
        random_project("Test Product", "D", ["Web", "Data Science"], [
            learner.oktaId for learner in learners
            if "Test Product - D" == learner.labsProject
        ]),
    ]
    return Payload(learners=learners, projects=projects)


if __name__ == '__main__':
    print(example_payload())
