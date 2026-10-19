(() => {
  const STORAGE_KEY = 'iro-demo-reports-v1';
  const sampleReports = [
    {id:'IRO-024',category:'Sanitation',area:'Akungba-Akoko',title:'Waste collection delay near campus',description:'Several shared collection points appear full. A clear collection update would help residents plan.',status:'In progress',date:'18 Oct 2026',urgency:'Soon',sample:true},
    {id:'IRO-023',category:'Roads & transport',area:'Iwaro',title:'Road surface needs attention',description:'A section of the route is difficult to use after rainfall. Please review drainage and repairs.',status:'Received',date:'16 Oct 2026',urgency:'Routine',sample:true},
    {id:'IRO-021',category:'Water & electricity',area:'AAUA campus',title:'Intermittent water supply',description:'Some shared facilities have had irregular water access. A service notice would be useful.',status:'In progress',date:'13 Oct 2026',urgency:'Soon',sample:true},
    {id:'IRO-018',category:'Facilities',area:'Etioro',title:'Street lighting repair completed',description:'A lighting fault was checked and the example report is marked resolved.',status:'Resolved',date:'08 Oct 2026',urgency:'Routine',sample:true}
  ];
  const issueList = document.getElementById('issueList');
  const form = document.getElementById('issueForm');
  const feedback = document.getElementById('formFeedback');
  let activeFilter = 'all';

  const escapeHTML = (value) => String(value).replace(/[&<>"']/g, (character) => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[character]));
  const getReports = () => {
    try {
      const saved = JSON.parse(localStorage.getItem(STORAGE_KEY));
      return Array.isArray(saved) ? [...saved, ...sampleReports] : sampleReports;
    } catch (_) { return sampleReports; }
  };
  const setReports = (reports) => {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(reports.filter((report) => !report.sample)));
      return true;
    } catch (_) { return false; }
  };

  function renderReports() {
    const reports = getReports();
    const openCount = reports.filter((item) => item.status !== 'Resolved').length;
    const resolvedCount = reports.length - openCount;
    document.getElementById('countAll').textContent = reports.length;
    document.getElementById('countOpen').textContent = openCount;
    document.getElementById('countResolved').textContent = resolvedCount;
    const visible = reports.filter((item) => activeFilter === 'all' || (activeFilter === 'resolved' ? item.status === 'Resolved' : item.status !== 'Resolved'));
    issueList.innerHTML = visible.length ? visible.map((item) => `
      <article class="issue-card">
        <div><div class="issue-meta"><span class="issue-category">${escapeHTML(item.category)}</span><span>·</span><span>${escapeHTML(item.area)}</span></div>
          <h3>${escapeHTML(item.title)}</h3><p>${escapeHTML(item.description)}</p></div>
        <span class="issue-status ${item.status === 'Resolved' ? 'resolved' : ''}">${escapeHTML(item.status)}</span>
        <div class="issue-foot"><span>${escapeHTML(item.id)} ${item.sample ? '· sample' : '· local demo'}</span><span>${escapeHTML(item.date)}</span></div>
      </article>`).join('') : '<p class="issue-empty">No reports match this filter yet.</p>';
  }

  document.querySelectorAll('[data-filter]').forEach((button) => button.addEventListener('click', () => {
    activeFilter = button.dataset.filter;
    document.querySelectorAll('[data-filter]').forEach((item) => item.classList.toggle('active', item === button));
    renderReports();
  }));

  document.getElementById('anonymous').addEventListener('change', (event) => {
    document.getElementById('contactWrap').hidden = event.target.checked;
  });

  form.addEventListener('submit', (event) => {
    event.preventDefault();
    if (!form.reportValidity()) return;
    const values = new FormData(form);
    const reports = getReports().filter((report) => !report.sample);
    const nextNumber = String(25 + reports.length).padStart(3, '0');
    reports.unshift({
      id:`IRO-${nextNumber}`,
      category:values.get('category'),
      area:values.get('area'),
      title:values.get('title'),
      description:values.get('description'),
      status:'Received',
      date:new Intl.DateTimeFormat('en-GB',{day:'2-digit',month:'short',year:'numeric'}).format(new Date()),
      urgency:values.get('urgency'),
      reporterGroup:values.get('reporterGroup'),
      anonymous:document.getElementById('anonymous').checked
    });
    const saved = setReports(reports);
    feedback.textContent = saved
      ? `Saved locally as ${reports[0].id}. This entry has not been sent to anyone.`
      : 'This browser could not save the entry. You can still review the example board.';
    form.reset();
    document.getElementById('contactWrap').hidden = true;
    activeFilter = 'all';
    document.querySelectorAll('[data-filter]').forEach((item) => item.classList.toggle('active', item.dataset.filter === 'all'));
    renderReports();
    document.getElementById('reports').scrollIntoView({behavior:'smooth',block:'start'});
  });

  renderReports();
})();
