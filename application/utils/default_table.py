from sqlalchemy.orm.session import Session

from application.database.connection import session_hook
from application.models.speciality import Specialization

specialization = [{"title": "Anatomical Pathology"}, {"title": "Anesthesiology"}, {"title": "Cardiology"}, {"title": "Cardiovascular/Thoracic Surgery"}, {"title": "Clinical Immunology/Allergy"},
    {"title": "Critical Care Medicine"}, {"title": "Dermatology"}, {"title": "Diagnostic Radiology"}, {"title": "Emergency Medicine"}, {"title": "Endocrinology and Metabolism"},
    {"title": "Family Medicine"}, {"title": "Gastroenterology"}, {"title": "General Internal Medicine"}, {"title": "General Surgery"}, {"title": "General/Clinical Pathology"},
    {"title": "Geriatric Medicine"}, {"title": "Hematology"}, {"title": "Medical Biochemistry"}, {"title": "Medical Genetics"}, {"title": "Medical Microbiology and Infectious Diseases"},
    {"title": "Medical Oncology"}, {"title": "Nephrology"}, {"title": "Neurology"}, {"title": "Neurosurgery"}, {"title": "Nuclear Medicine"}, {"title": "Obstetrics/Gynecology"},
    {"title": "Occupational Medicine"}, {"title": "Ophthalmology"}, {"title": "Orthopedic Surgery"}, {"title": "Otolaryngology"}, {"title": "Pediatrics"},
    {"title": "Physical Medicine and Rehabilitation (PM & R)"}, {"title": "Plastic Surgery"}, {"title": "Psychiatry"}, {"title": "Public Health and Preventive Medicine (PhPm)"},
    {"title": "Radiation Oncology"}, {"title": "Respirology"}, {"title": "Rheumatology"}, {"title": "Urology"}, {"title": "Conclusion"}]


@session_hook
def bulk_create_specialization(db: Session) -> None:
    objects = []
    for speciality in specialization:
        if Specialization.get_speciality_by_title(speciality['title']) is None:
            objects.append(Specialization(**speciality))

    db.bulk_save_objects(objects)
    db.flush()


# call the method to create the specializations
def run():
    bulk_create_specialization()