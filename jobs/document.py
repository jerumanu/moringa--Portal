from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Category, Job, JobSkill, JobResponsibility, JobQualification

@registry.register_document
class JobDocument(Document):
    job_skills = fields.NestedField(properties={
        'skill_name': fields.TextField()
    })
    job_responsibilities = fields.NestedField(properties={
        'responsibility_name': fields.TextField()
    })
    job_qualifications = fields.NestedField(properties={
        'qualification_name': fields.TextField()
    })

    class Index:
        name = 'job_index'
    
    class Django:
        model = Category
        fields = ['job_title', 'job_detail', 'job_level', 'dateline', 'posted_on']
        related_models = [JobSkill, JobResponsibility, JobQualification]
