"""No-code ops-stack fingerprints (added for Skofi's ICP)."""

from harvey.integrations.tech_detect import detect_tech


def test_detects_embedded_no_code_tools():
    html = """
    <iframe src="https://airtable.com/embed/shrAbCdEfGh123456"></iframe>
    <iframe src="https://forms.monday.com/forms/abc123"></iframe>
    <form action="https://hook.eu2.make.com/xyz"></form>
    <script src="https://interfaces.zapier.com/assets/web-components/zapier-interfaces.js"></script>
    <a href="https://acme.app.n8n.cloud/form/1">form</a>
    <iframe src="https://tally.so/embed/w4bc"></iframe>
    """
    found = detect_tech(html)
    for tool in ("Airtable", "monday.com", "Make", "Zapier", "n8n", "Tally"):
        assert tool in found


def test_plain_mentions_do_not_match():
    html = "<p>We use Airtable, monday and Zapier internally. Make it happen.</p>"
    found = detect_tech(html)
    assert not {"Airtable", "monday.com", "Make", "Zapier"} & set(found)
