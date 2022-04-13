from app.data_models import Payload, Project


def get_team_name(project: Project) -> str:
    product_name = project.product
    team_code = project.teamCode
    return f"{product_name} - {team_code}"


def hat_trick(payload: Payload) -> Payload:

    project_lookup = {
        project.id: idx for idx, project in enumerate(payload.projects)
    }
    learner_lookup = {
        learner.lambdaId: idx for idx, learner in enumerate(payload.learners)
    }

    tpms = sorted(payload.learners, key=lambda x: x.tpmInterestRank)
    ds_tpms = list(filter(lambda x: x.track == "DS", tpms))
    web_tpms = list(filter(lambda x: x.track == "Web", tpms))

    project_ids = map(lambda x: x.id, payload.projects)
    ds_project_ids = map(lambda x: x.id, filter(lambda x: "DS" in x.tracks, payload.projects))
    web_project_ids = map(lambda x: x.id, filter(lambda x: len(x.tracks) == 1, payload.projects))

    placed = set()

    for project in payload.projects:
        placed.union(project.teamMemberSmtIds)

    for learner in payload.learners:
        if learner.labsProject != "":
            placed.add(learner.lambdaId)

    def place_learner(learner_id: str, project_idx: str):
        placed.add(learner_id)
        payload.projects[
            project_lookup[project_idx]
        ].teamMemberSmtIds.append(learner_id)
        payload.learners[
            learner_lookup[learner_id]
        ].labsProject = project_idx

    for ds_project_id in ds_project_ids:
        if ds_tpms:
            ds_tpm = ds_tpms.pop()
            while ds_tpm.lambdaId in placed and ds_tpms:
                ds_tpm = ds_tpms.pop()
            place_learner(ds_tpm.lambdaId, ds_project_id)

    for web_project_id in web_project_ids:
        if web_tpms:
            web_tpm = web_tpms.pop()
            while web_tpm.lambdaId in placed and web_tpms:
                web_tpm = web_tpms.pop()
            place_learner(web_tpm.lambdaId, web_project_id)

    for project_id in project_ids:
        if web_tpms:
            web_tpm = web_tpms.pop()
            while web_tpm.lambdaId in placed and web_tpms:
                web_tpm = web_tpms.pop()
            place_learner(web_tpm.lambdaId, project_id)

    for learner in payload.learners:
        if learner.lambdaId not in placed:
            if learner.track == "DS":
                smallest = min(
                    filter(lambda x: "DS" in x.tracks, payload.projects),
                    key=lambda x: len(x.teamMemberSmtIds),
                )
                place_learner(learner.lambdaId, smallest.id)
            else:
                smallest = min(
                    payload.projects,
                    key=lambda x: len(x.teamMemberSmtIds),
                )
                place_learner(learner.lambdaId, smallest.id)

    return payload
