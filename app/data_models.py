from random import randint, choice
from typing import Optional, List

from pydantic import BaseModel

from app.generators import generate_uuid, random_track, NameGenerator


class Learner(BaseModel):
    lambdaId: str
    name: str
    track: str
    labsProject: Optional[str]
    gitExpertise: int
    dockerExpertise: int
    playByEar: int
    detailOriented: int
    speakUpInDiscussions: int
    soloOrSocial: str
    meaningOrValue: str
    feelsRightOrMakesSense: str
    favoriteOrCollect: str
    tpmSkill1: Optional[str]
    tpmSkill2: Optional[str]
    tpmSkill3: Optional[str]
    tpmInterest1: Optional[int] = 0
    tpmInterest2: Optional[int] = 0
    tpmInterest3: Optional[int] = 0
    tpmInterest4: Optional[int] = 0
    uxInterest1: Optional[int] = 0
    uxInterest2: Optional[int] = 0
    frontendInterest1: Optional[int] = 0
    frontendInterest2: Optional[int] = 0
    backendInterest1: Optional[int] = 0
    backendInterest2: Optional[int] = 0
    dataEngInterest1: Optional[int] = 0
    dataEngInterest2: Optional[int] = 0
    dataEngInterest3: Optional[int] = 0
    mlEngInterest1: Optional[int] = 0
    mlEngInterest2: Optional[int] = 0
    mlEngInterest3: Optional[int] = 0
    mlOpsInterest1: Optional[int] = 0
    mlOpsInterest2: Optional[int] = 0
    mlOpsInterest3: Optional[int] = 0
    tpmSkillRank: Optional[float]
    tpmInterestRank: Optional[float]
    uxInterestRank: Optional[float]
    frontendInterestRank: Optional[float]
    backendInterestRank: Optional[float]
    dataEngInterestRank: Optional[float]
    mlEngInterestRank: Optional[float]
    mlOpsInterestRank: Optional[float]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        skill_score = [
            1 if self.tpmSkill1 == "B" else 0,
            1 if self.tpmSkill2 == "B" else 0,
            1 if self.tpmSkill3 == "C" else 0,
        ]
        self.tpmSkillRank = sum(skill_score) / 3
        self.tpmInterestRank = sum([
            self.tpmInterest1,
            self.tpmInterest2,
            self.tpmInterest3,
            self.tpmInterest4,
        ]) / 16

        if self.track == "Web":
            self.uxInterest1 = randint(1, 4)
            self.uxInterest2 = randint(1, 4)
            self.uxInterestRank = sum([
                self.uxInterest1,
                self.uxInterest2],
            ) / 8
            self.frontendInterest1 = randint(1, 4)
            self.frontendInterest2 = randint(1, 4)
            self.frontendInterestRank = sum([
                self.frontendInterest1,
                self.frontendInterest2],
            ) / 8
            self.backendInterest1 = randint(1, 4)
            self.backendInterest2 = randint(1, 4)
            self.backendInterestRank = sum([
                self.backendInterest1,
                self.backendInterest2,
            ]) / 8

        elif self.track == "DS":
            self.dataEngInterest1 = randint(1, 4)
            self.dataEngInterest2 = randint(1, 4)
            self.dataEngInterest3 = randint(1, 4)
            self.dataEngInterestRank = sum([
                self.dataEngInterest1,
                self.dataEngInterest2,
                self.dataEngInterest3
            ]) / 12

            self.mlEngInterest1 = randint(1, 4)
            self.mlEngInterest2 = randint(1, 4)
            self.mlEngInterest3 = randint(1, 4)
            self.mlEngInterestRank = sum([
                self.mlEngInterest1,
                self.mlEngInterest2,
                self.mlEngInterest3
            ]) / 12

            self.mlOpsInterest1 = randint(1, 4)
            self.mlOpsInterest2 = randint(1, 4)
            self.mlOpsInterest3 = randint(1, 4)
            self.mlOpsInterestRank = sum([
                self.mlOpsInterest1,
                self.mlOpsInterest2,
                self.mlOpsInterest3,
            ]) / 12


class Project(BaseModel):
    id: str
    product: str
    teamCode: str
    tracks: List[str]
    releaseManager: str
    teamMemberSmtIds: List[str] = []


class Payload(BaseModel):
    learners: List[Learner] = [Learner(
        lambdaId=generate_uuid(16),
        name=NameGenerator.generate_name(),
        track=random_track(),
        labsProject="",
        gitExpertise=randint(1, 5),
        dockerExpertise=randint(1, 5),
        playByEar=randint(1, 5),
        detailOriented=randint(1, 5),
        speakUpInDiscussions=randint(1, 5),
        soloOrSocial=choice(["A", "B"]),
        meaningOrValue=choice(["A", "B"]),
        feelsRightOrMakesSense=choice(["A", "B"]),
        favoriteOrCollect=choice(["A", "B"]),
        tpmSkill1=choice(["A", "B", "C"]),  # B
        tpmSkill2=choice(["A", "B", "C"]),  # B
        tpmSkill3=choice(["A", "B", "C"]),  # C
        tpmInterest1=randint(1, 4),
        tpmInterest2=randint(1, 4),
        tpmInterest3=randint(1, 4),
        tpmInterest4=randint(1, 4),
    ) for _ in range(50)]
    projects: List[Project] = [
        Project(
            id=generate_uuid(8),
            product="Test Product",
            teamCode="A",
            releaseManager=NameGenerator.generate_name(),
            tracks=["Web"],
        ),
        Project(
            id=generate_uuid(8),
            product="Test Product",
            teamCode="B",
            releaseManager=NameGenerator.generate_name(),
            tracks=["Web", "DS"]
        ),
        Project(
            id=generate_uuid(8),
            product="Test Product",
            teamCode="C",
            releaseManager=NameGenerator.generate_name(),
            tracks=["Web", "DS"]
        ),
        Project(
            id=generate_uuid(8),
            product="Test Product",
            teamCode="D",
            releaseManager=NameGenerator.generate_name(),
            tracks=["Web", "DS"]
        ),
        Project(
            id=generate_uuid(8),
            product="Test Product",
            teamCode="E",
            releaseManager=NameGenerator.generate_name(),
            tracks=["Web", "BD"]
        )
    ]
