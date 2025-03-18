document.addEventListener('DOMContentLoaded', function() {
    // normalise URL - remove trailing backslash
    const referrer = document.referrer.replace(/\/$/, '');
    const prevPageContainer = document.getElementById('prev-page-link');
    const prevLinkText = referrer.split('/').pop().replaceAll('-', ' ');

    let link = `← Go back to `;

    if (referrer && new URL(referrer).origin === window.location.origin && prevLinkText !== "projects") {
         link += `
                <a href="${referrer}" class="back-link"> ${prevLinkText}</a> or see `;
    }

    link += `<a href="/projects">all our projects</a>`;

    prevPageContainer.innerHTML = link;
});