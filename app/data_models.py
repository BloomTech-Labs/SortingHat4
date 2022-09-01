from typing import Optional, List, Literal

from pydantic import BaseModel


class Learner(BaseModel):
    oktaId: str
    name: str
    track: str
    storyPoints: Optional[int] = 0
    labsProject: Optional[str] = ""
    labsTimeSlot: Optional[List[str]] = [""]
    gitHubHandle: Optional[str] = ""
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


class Project(BaseModel):
    id: str
    product: str
    teamCode: str
    tracks: List[str]
    releaseManager: str
    teamMemberSmtIds: List[str] = []


class Payload(BaseModel):
    learners: List[Learner]
    projects: List[Project]


SoloSocial = Literal["solo", "social"]
MeaningValue = Literal["meaning", "value"]
FeelSense = Literal["feel", "sense"]
FavoriteCollect = Literal["favorite", "collect"]
