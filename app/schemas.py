from pydantic import BaseModel
from typing import List
from app.models import Term

class TermResponse(BaseModel):
    class Config:
        from_attributes = True
        populate_by_name = True

    id: int
    subject_en: str | None = None
    term_en: str | None = None
    term_en_parameter: str | None = None
    abbreviation_en: str | None = None
    abbreviation_en_parameter: str | None = None
    synonyms_en: str | None = None
    synonyms_en_parameters: str | None = None
    textual_support_1_en: str | None = None
    textual_support_2_en: str | None = None
    textual_support_3_en: str | None = None
    domaine_fr: str | None = None
    terme_fr: str | None = None
    terme_fr_parametre: str | None = None
    abbreviation_fr: str | None = None
    abbreviation_fr_parametre: str | None = None
    synonymes_fr: str | None = None
    synonymes_fr_parametre: str | None = None
    justification_1_fr: str | None = None
    justification_2_fr: str | None = None
    justification_3_fr: str | None = None
    universal_entries: str | None = None
    dom_subj_es: str | None = None
    terme_term_es: str | None = None
    terme_term_param_es: str | None = None
    abbr_es: str | None = None
    abbr_param_es: str | None = None
    syno_es: str | None = None
    syno_param_es: str | None = None
    just_textsupp_1_es: str | None = None
    just_textsupp_2_es: str | None = None
    just_textsupp_3_es: str | None = None
    dom_subj_pt: str | None = None
    terme_term_pt: str | None = None
    terme_term_param_pt: str | None = None
    abbr_pt: str | None = None
    abbr_param_pt: str | None = None
    syno_pt: str | None = None
    syno_param_pt: str | None = None
    just_textsupp_1_pt: str | None = None
    just_textsupp_2_pt: str | None = None
    just_textsupp_3_pt: str | None = None

class TermsResponse(BaseModel):
    count: int
    results: List[TermResponse]