from odoo import api, fields, models


class CustomCrm(models.Model):
    _name = 'crm.lead'
    _description = 'New Description'
    _inherit = 'crm.lead'

    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female'), ], 'Gender', default='male')
    course_applying_for = fields.Selection([('coreProgramInDataScienceAi', 'Core Program in Data Science & AI'),
                                            ('foundationsProgramOfDataScience',
                                             'Foundations Program of Data Science'),
                                            ('softwareEngineering', 'Software Engineering')],
                                           'Which Course are you applying for?', default='coreProgramInDataScienceAi')
    intake = fields.Selection(
        [('may2022', 'May 2022')], 'Which Intake Are You Applying For?', default='may2022')
    education_level = fields.Selection(
        [('phD', 'PhD'), ('masters', 'Masters'), ('bachelors', 'Bachelors'),
         ('diploma', 'Diploma'), ('certificate', 'Certificate')])
    course_of_study = fields.Char('Your Course of Study')
    university_attended = fields.Char('University/Institution Attended?')
    occupation = fields.Char('What is Your Current Occupation?')
    employment_status = fields.Selection(
        [('partTimeEmployee', 'Part-Time Employee'), ('intern', 'Intern'),
         ('Self-Employed', 'selfEmployed'), ('student', 'Student'), ('unemployed', 'Unemployed')],
        'Current Status', default='')
    organization = fields.Char('Organization/Institution')
    source = fields.Selection([(
        "facebook", "Facebook"

    ),
        (
        "email",
        "Email"

    ),
        (
        "googleSearch",
        "Google search"

    ),
        (
        "instagram",
        "Instagram"

    ),
        (
        "twitter",
        "Twitter"

    ),
        (
        "aFriendReferral",
        "A Friend Referral"
    ),
        (
        "whatsapp",
        "Whatsapp"
    ),
        (
        "jengaStaff",
        "JENGA Staff",

    ), (
        "jengaStudent",
        "JENGA Student",

    ),
        (
        "jengaEvent",
        "JENGA Event"

    )], 'Where did you hear about us?', default='email')
    # tag_ids = fields.Many2many(
    #     'crm.tag', 'crm_tag_rel', 'crm.custom.tag_ids', 'tag_id', string='Tags',
    #     help="Classify and analyze your lead/opportunity categories like: Training, Service")
