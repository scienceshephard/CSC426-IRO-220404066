/**
 * Creates the IRO anonymous needs-assessment questionnaire in the signed-in
 * Google account. Run createIROSurvey once, then copy the URLs from the log.
 * The script creates the form only; it does not submit or invent responses.
 */
function createIROSurvey() {
  const form = FormApp.create('IRO (Issues Reporting Outlet) — Community Needs Survey', false);
  form
    .setDescription(
      'This short questionnaire gathers views from AAUA students and residents of Akungba, Iwaro, Etioro, Ayegunle, and nearby communities. It informs a CSC426 coursework prototype. Participation is voluntary. Do not include names, phone numbers, exact addresses, health details, allegations about named people, or other identifying information. The form does not collect email addresses. Responses are for coursework analysis and are not an emergency or complaint-handling service.'
    )
    .setCollectEmail(false)
    .setAllowResponseEdits(false)
    .setProgressBar(true)
    .setConfirmationMessage('Thank you. Your anonymous feedback has been recorded for the IRO coursework needs assessment.');

  addChoice(form, 'Consent', 'I understand the purpose above and choose to provide anonymous feedback.', [
    'Yes, I consent to take part',
    'No, I do not consent'
  ], true);

  addChoice(form, 'Respondent group', 'Which group best describes you?', [
    'AAUA student', 'Akungba indigene/resident', 'Iwaro indigene/resident',
    'Etioro indigene/resident', 'Ayegunle indigene/resident', 'Other nearby community member', 'Prefer not to say'
  ], true, true);

  addChoice(form, 'Main area', 'Which broad area are you answering about?', [
    'AAUA campus', 'Akungba-Akoko', 'Iwaro', 'Etioro', 'Ayegunle', 'Other nearby area', 'Prefer not to say'
  ], true, true);

  addChoice(form, 'Recent issues', 'In the past six months, have you experienced or witnessed an unresolved community or campus issue?', [
    'Yes', 'No', 'Not sure', 'Prefer not to say'
  ], true);

  addChecks(form, 'Issue types', 'Which issues have you experienced or witnessed? Select all that apply.', [
    'Roads and transport', 'Water and electricity', 'Sanitation and waste',
    'Safety and security', 'Facilities and maintenance', 'Student services',
    'Communication or delayed updates', 'Other', 'Prefer not to say'
  ], false);

  addChoice(form, 'Issue frequency', 'How often do issues that need attention affect your area?', [
    'Weekly or more often', 'About monthly', 'A few times a year', 'Rarely', 'Not sure', 'Prefer not to say'
  ], true);

  addChecks(form, 'Reporting barriers', 'What makes it difficult to report an issue or get follow-up? Select all that apply.', [
    'I do not know the right contact or channel', 'I am concerned about privacy',
    'I am concerned about retaliation', 'I expect no response or update',
    'The process takes too much time', 'I do not have reliable internet/access',
    'I have not had a reason to report', 'Other', 'Prefer not to say'
  ], false);

  addChoice(form, 'Current reporting channel', 'How would you most likely raise an issue today?', [
    'Tell a representative or community leader', 'Contact a university/community office',
    'Use a phone call or message', 'Post in a group or on social media',
    'I would not report it', 'Prefer not to say'
  ], true, true);

  addChoice(form, 'Privacy confidence', 'How confident would you feel using a reporting service that does not require your name?', [
    'Very confident', 'Somewhat confident', 'Neither confident nor concerned',
    'Somewhat concerned', 'Very concerned', 'Not sure'
  ], true);

  addChoice(form, 'Status updates', 'Which follow-up would be most useful?', [
    'A reference number and status page', 'A message when the status changes',
    'A public summary with no reporter details', 'A direct response from a coordinator',
    'No follow-up needed'
  ], true, true);

  addChoice(form, 'First update expectation', 'How soon should a coordinator acknowledge a non-emergency report?', [
    'Within one working day', 'Within three working days', 'Within one week',
    'Within two weeks', 'I am not sure'
  ], true);

  addChecks(form, 'Helpful features', 'Which features would make the service useful to you? Select all that apply.', [
    'Anonymous reporting', 'Clear issue categories', 'A safe way to identify a broad location',
    'A reference number', 'Progress/status updates', 'A way to correct or add context',
    'A contact point for urgent safety matters', 'Other'
  ], false);

  form.addParagraphTextItem()
    .setTitle('Anything else?')
    .setHelpText('Optional. Suggest improvements without naming people or including private or identifying details.')
    .setRequired(false);

  form.setPublished(true);
  Logger.log('Responder URL: ' + form.getPublishedUrl());
  Logger.log('Editor URL: ' + form.getEditUrl());
}

function addChoice(form, title, question, options, required, other) {
  const item = form.addMultipleChoiceItem().setTitle(question).setChoiceValues(options).setRequired(required);
  if (other) item.showOtherOption(true);
  item.setHelpText(title);
  return item;
}

function addChecks(form, title, question, options, required) {
  return form.addCheckboxItem()
    .setTitle(question)
    .setHelpText(title)
    .setChoiceValues(options)
    .setRequired(required);
}
