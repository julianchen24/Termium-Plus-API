from sqlmodel import Field, SQLModel
from typing import Optional

class Term(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    # English Fields
    subject_en: Optional[str] = None
    term_en: Optional[str] = Field(index=True)
    term_en_parameter: Optional[str] = None
    abbreviation_en: Optional[str] = None
    abbreviation_en_parameter: Optional[str] = None
    synonyms_en: Optional[str] = None
    synonyms_en_parameters: Optional[str] = None
    textual_support_1_en: Optional[str] = None
    textual_support_2_en: Optional[str] = None
    textual_support_3_en: Optional[str] = None

    # French fields
    domaine_fr: Optional[str] = None
    terme_fr: Optional[str] = Field(index=True)
    terme_fr_parametre: Optional[str] = None
    abbreviation_fr: Optional[str] = None
    abbreviation_fr_parametre: Optional[str] = None
    synonymes_fr: Optional[str] = None
    synonymes_fr_parametre: Optional[str] = None
    justification_1_fr: Optional[str] = None
    justification_2_fr: Optional[str] = None
    justification_3_fr: Optional[str] = None

    # Universal entries
    universal_entries: Optional[str] = None

    # Spanish fields
    dom_subj_es: Optional[str] = None
    terme_term_es: Optional[str] = Field(index=True)
    terme_term_param_es: Optional[str] = None
    abbr_es: Optional[str] = None
    abbr_param_es: Optional[str] = None
    syno_es: Optional[str] = None
    syno_param_es: Optional[str] = None
    just_textsupp_1_es: Optional[str] = None
    just_textsupp_2_es: Optional[str] = None
    just_textsupp_3_es: Optional[str] = None

    # Portuguese fields
    dom_subj_pt: Optional[str] = None
    terme_term_pt: Optional[str] = Field(index=True)
    terme_term_param_pt: Optional[str] = None
    abbr_pt: Optional[str] = None
    abbr_param_pt: Optional[str] = None
    syno_pt: Optional[str] = None
    syno_param_pt: Optional[str] = None
    just_textsupp_1_pt: Optional[str] = None
    just_textsupp_2_pt: Optional[str] = None
    just_textsupp_3_pt: Optional[str] = None

    





