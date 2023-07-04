
# from django_elasticsearch_dsl import Document, fields
# from django_elasticsearch_dsl.registries import registry

# from authentication.models import User
# from jobs.models import Category, JobDetail, Qualification, Responsibility, Skill



# @registry.register_document
# class UserDocument(Document):
#     class Index:
#         name = 'users'
#         settings = {
#             'number_of_shards': 1,
#             'number_of_replicas': 0,
#         }

#     class Django:
#         model = User
#         fields = [
#             'id',
#             'first_name',
#             'last_name',
        
#         ]
# @registry.register_document
# class QualificationDocument(Document):
#     class Index:
#         name = 'qualifications'
#         settings = {
#             'number_of_shards': 1,
#             'number_of_replicas': 0,
#         }

#     class Django:
#         model = Qualification
#         fields = [
#             'id',
#             'qualification_name',
            
#         ]

# @registry.register_document
# class  ResponsibilityDocument(Document):
#     class Index:
#         name = 'responsibilities'
#         settings = {
#             'number_of_shards': 1,
#             'number_of_replicas': 0,
#         }

#     class Django:
#         model = Responsibility
#         fields = [
#             'id',
#             'responsibility_name',
            
#         ]

# @registry.register_document
# class SkillsDocument(Document):

#     class Index:
#         name = 'skills'
#         settings = {
#             'number_of_shards': 1,
#             'number_of_replicas': 0,
#         }

#     class Django:
#         model = Skill
#         fields = [
#             # 'id',
#             'skill_name',
            
#         ]

# class JobDetailDocument(Document):
#     job_responsibilities = fields.ObjectField(properties={
#         'id': fields.IntegerField(),
#         'responsibility_name': fields.TextField(),
#     })
#     job_qualifications = fields.ObjectField(properties={
#         'id': fields.IntegerField(),
#         'qualification_name': fields.TextField(),
#     })
#     job_skills = fields.ObjectField(properties={
#         'skill_name': fields.TextField(),
#     })

#     class Index:
#         name = 'job_details'
#         settings = {
#             'number_of_shards': 1,
#             'number_of_replicas': 0,
#         }

#     class Django:
#         model = JobDetail
#         fields = [
#             'job_title',
#             'job_level',
#             'job_detail',
#             'dateline',
#             'posted_on',
#         ]

#     def prepare_job_skills(self, instance):
#         skills_data = []
#         for skill in instance.job_skills.all():
#             skills_data.append({
#                 'skill_name': skill.skill_name,
#             })
#         return skills_data

# @registry.register_document
# class CategoryDocument(Document):

    
#     job_details= fields.ObjectField(properties={
#         'id': fields.IntegerField(),
#         'job_title': fields.TextField(),
#         'job_detail':fields.TextField(),
#         'job_level': fields.TextField(),
#         'dateline':fields.DateField(),
#         'posted_on':fields.DateField(),
        
#     })

    
#     class Index:
#         name = 'categories'
#         settings = {
#             'number_of_shards': 1,
#             'number_of_replicas': 0,
#         }

#     class Django:
#         model = Category
#         fields = [
            
#             'title',
#             'position',
#             'location',
        
#         ]


