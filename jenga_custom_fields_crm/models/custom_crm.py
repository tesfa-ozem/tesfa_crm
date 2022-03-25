from odoo import api, fields, models


class CustomCrm(models.Model):
    _description = 'New Description'
    _inherit = 'crm.lead'

    gender = fields.Selection(
        [('Male', 'Male'), ('Female', 'Female'), ('Prefer not to say', 'Prefer Not To Say')], 'Gender', default='Male')
    course_applying_for = fields.Selection([('Core Course in Data Science & AI', 'Core Course in Data Science & AI'),
                                            ('Foundations Course of Data Science',
                                             'Foundations Course of Data Science'),
                                            ('Software Engineering', 'Software Engineering')],
                                           'Which Course are you applying for?', default='')
    intake = fields.Char('Which Intake Are You Applying For?')
    education_level = fields.Selection(
        [('Phd', 'Phd'), ('Masters', 'Masters'), ('Bachelors', 'Bachelors'),
         ('Diploma', 'Diploma'), ('Certificate', 'Certificate')])
    course_of_study = fields.Char('Your Course of Study')
    university_attended = fields.Char('University/Institution Attended?')
    occupation = fields.Char('What is Your Current Occupation?')
    employment_status = fields.Selection(
        [('Full-Time Employee', 'Full-Time Employee'), ('Unemployed', 'Unemployed'),
         ('Student', 'Student'), ('Intern', 'Intern'), ('Part-Time Employee', 'Part-Time Employee')],
        'Current Status', default='')
    organization = fields.Char('Organization/Institution')
    source = fields.Selection([(
        "facebook", "Facebook"

    ),
        (
        "Email",
        "Email"

    ),
        (
        "Google search",
        "Google search"

    ),
        (
        "Instagram",
        "Instagram"

    ),
        (
        "Twitter",
        "Twitter"

    ),
        (
        "A Friend Referral",
        "A Friend Referral"
    ),
        (
        "Whatsapp",
        "Whatsapp"
    ),
        (
        "JENGA Staff",
        "JENGA Staff",

    ), (
        "JENGA Student",
        "JENGA Student",

    ),
        (
        "JENGA Event",
        "JENGA Event"

    )], 'Where did you hear about us?', default='')
    # tag_ids = fields.Many2many(
    #     'crm.tag', 'crm_tag_rel', 'crm.custom.tag_ids', 'tag_id', string='Tags',
    #     help="Classify and analyze your lead/opportunity categories like: Training, Service")
