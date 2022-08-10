from typing import Optional, List

from pydantic import BaseModel


class Learner(BaseModel):
    lambdaId: str
    name: str
    track: str
    storyPoints: Optional[int] = 0
    labsProject: Optional[str] = ""
    gitExpertise: Optional[int] = 0
    dockerExpertise: Optional[int] = 0
    playByEar: Optional[int] = 0
    detailOriented: Optional[int] = 0
    speakUpInDiscussions: Optional[int] = 0
    soloOrSocial: Optional[str] = ""
    meaningOrValue: Optional[str] = ""
    feelsRightOrMakesSense: Optional[str] = ""
    favoriteOrCollect: Optional[str] = ""
    tpmSkill1: Optional[str] = ""
    tpmSkill2: Optional[str] = ""
    tpmSkill3: Optional[str] = ""
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
    tpmSkillRank: Optional[float] = 0
    tpmInterestRank: Optional[float] = 0
    uxInterestRank: Optional[float] = 0
    frontendInterestRank: Optional[float] = 0
    backendInterestRank: Optional[float] = 0
    dataEngInterestRank: Optional[float] = 0
    mlEngInterestRank: Optional[float] = 0
    mlOpsInterestRank: Optional[float] = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tpmSkillRank = sum([
            self.tpmSkill1 == "B",
            self.tpmSkill2 == "B",
            self.tpmSkill3 == "C",
        ]) / 3
        self.tpmInterestRank = sum([
            self.tpmInterest1,
            self.tpmInterest2,
            self.tpmInterest3,
            self.tpmInterest4,
        ]) / 16
        self.uxInterestRank = sum([
            self.uxInterest1,
            self.uxInterest2,
        ]) / 8
        self.frontendInterestRank = sum([
            self.frontendInterest1,
            self.frontendInterest2,
        ]) / 8
        self.backendInterestRank = sum([
            self.backendInterest1,
            self.backendInterest2,
        ]) / 8
        self.dataEngInterestRank = sum([
            self.dataEngInterest1,
            self.dataEngInterest2,
            self.dataEngInterest3,
        ]) / 12
        self.mlEngInterestRank = sum([
            self.mlEngInterest1,
            self.mlEngInterest2,
            self.mlEngInterest3,
        ]) / 12
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
    storyPointTotal: Optional[int] = 0


class Payload(BaseModel):
    learners: List[Learner]
    projects: List[Project]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for learner in self.learners:
            for project in self.projects:
                if project.id == learner.labsProject:
                    project.storyPointTotal += learner.storyPoints
