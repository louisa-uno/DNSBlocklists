## This is a blocklist for AdGuard and Pi-hole which combines many of the best blocklists

[![Update blocklist](https://github.com/louisa-uno/DNSBlocklists/actions/workflows/update-blocklist.yml/badge.svg)](https://github.com/louisa-uno/DNSBlocklists/actions/workflows/update-blocklist.yml)
[![GitHub last commit (branch)](https://img.shields.io/github/last-commit/louisa-uno/DNSBlocklists/auto-update?label=Last%20DNS%20blocklist%20update)](https://github.com/louisa-uno/DNSBlocklists/actions/workflows/update-blocklist.yml)

[![DeepSource](https://deepsource.io/gh/louisa-uno/DNSBlocklists.svg/?label=active+issues&show_trend=true&token=A9moFT741YyFRfhQ97zeWwKL)](https://deepsource.io/gh/louisa-uno/DNSBlocklists/?ref=repository-badge)
[![built with: Python3](https://camo.githubusercontent.com/0d9fbff04202da688cc79c5ffe984bd171edf453b2e41e5e56e55202dd5bdbb2/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6275696c74253230776974682d507974686f6e332d7265642e737667)](https://www.python.org/)

## 📝 Usage

Add the following all categories or a few of them to your AdGuard or Pi-hole blocklists

If you do want an optimized list for either AdGuard or Pi-hole replace the url ending `.txt` with `.adguard` or `.pihole`

| Category             | File url                                                                                          |
| -------------------- | ------------------------------------------------------------------------------------------------- |
| All categories       | `https://raw.githubusercontent.com/louisa-uno/DNSBlocklists/auto-update/list.txt`                 |
| Suspicious           | `https://raw.githubusercontent.com/louisa-uno/DNSBlocklists/auto-update/Suspicious.txt`           |
| Advertising          | `https://raw.githubusercontent.com/louisa-uno/DNSBlocklists/auto-update/Advertising.txt`          |
| Tracking & Telemetry | `https://raw.githubusercontent.com/louisa-uno/DNSBlocklists/auto-update/TrackingAndTelemetry.txt` |
| Malicious            | `https://raw.githubusercontent.com/louisa-uno/DNSBlocklists/auto-update/Malicious.txt`            |
| Facebook             | `https://raw.githubusercontent.com/louisa-uno/DNSBlocklists/auto-update/Facebook.txt`             |
| Adult content        | `https://raw.githubusercontent.com/louisa-uno/DNSBlocklists/auto-update/Adult content.txt`        |

## 🌟 Credits

<!-- MARKDOWN-AUTO-DOCS:START (JSON_TO_HTML_TABLE:src=./lists.json) -->
<table class="JSON-TO-HTML-TABLE"><thead><tr><th class="category-th">category</th><th class="name-th">name</th><th class="url-th">url</th><th class="site-url-th">site_url</th><th class="license-th">license</th></tr></thead><tbody ><tr ><td class="category-td td_text">Suspicious</td><td class="name-td td_text">FadeMind-Spam</td><td class="url-td td_text">https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.Spam/hosts</td><td class="site-url-td td_text">https://github.com/FadeMind/hosts.extras</td><td class="license-td td_text">GPLv3+</td></tr>
<tr ><td class="category-td td_text">Suspicious</td><td class="name-td td_text">matomo-org-referrer-spam-list</td><td class="url-td td_text">https://raw.githubusercontent.com/matomo-org/referrer-spam-blacklist/master/spammers.txt</td><td class="site-url-td td_text">https://github.com/matomo-org/referrer-spam-list</td><td class="license-td td_text">PDM</td></tr>
<tr ><td class="category-td td_text">Advertising</td><td class="name-td td_text">adaway-org</td><td class="url-td td_text">https://adaway.org/hosts.txt</td><td class="site-url-td td_text">https://adaway.org/</td><td class="license-td td_text">undefined</td></tr>
<tr ><td class="category-td td_text">Advertising</td><td class="name-td td_text">AdguardTeam-AdGuardSDNSFilter</td><td class="url-td td_text">https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt</td><td class="site-url-td td_text">https://github.com/AdguardTeam/AdGuardSDNSFilter</td><td class="license-td td_text">GPLv3</td></tr>
<tr ><td class="category-td td_text">Advertising</td><td class="name-td td_text">anudeepND-blacklist-adservers</td><td class="url-td td_text">https://raw.githubusercontent.com/anudeepND/blacklist/master/adservers.txt</td><td class="site-url-td td_text">https://github.com/anudeepND/blacklist</td><td class="license-td td_text">MIT</td></tr>
<tr ><td class="category-td td_text">Advertising</td><td class="name-td td_text">lists.disconnect.me-simple_ad.txt</td><td class="url-td td_text">https://s3.amazonaws.com/lists.disconnect.me/simple_ad.txt</td><td class="site-url-td td_text">https://disconnect.me/</td><td class="license-td td_text">undefined</td></tr>
<tr ><td class="category-td td_text">Advertising</td><td class="name-td td_text">Easylist</td><td class="url-td td_text">https://raw.githubusercontent.com/easylist/easylist/master/easylist/easylist_adservers.txt</td><td class="site-url-td td_text">https://easylist.to/</td><td class="license-td td_text">GPLv3</td></tr>
<tr ><td class="category-td td_text">Advertising</td><td class="name-td td_text">UncheckyAds</td><td class="url-td td_text">https://raw.githubusercontent.com/FadeMind/hosts.extras/master/UncheckyAds/hosts</td><td class="site-url-td td_text">https://unchecky.com/</td><td class="license-td td_text">MIT</td></tr>
<tr ><td class="category-td td_text">Advertising</td><td class="name-td td_text">bigdargon-hostsVN</td><td class="url-td td_text">https://raw.githubusercontent.com/bigdargon/hostsVN/master/hosts</td><td class="site-url-td td_text">https://github.com/bigdargon/hostsVN</td><td class="license-td td_text">MIT</td></tr>
<tr ><td class="category-td td_text">TrackingAndTelemetry</td><td class="name-td td_text">FadeMind-2o7Net</td><td class="url-td td_text">https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.2o7Net/hosts</td><td class="site-url-td td_text">http://hostsfile.org/hosts.html</td><td class="license-td td_text">GPLv3+</td></tr>
<tr ><td class="category-td td_text">TrackingAndTelemetry</td><td class="name-td td_text">crazy-max-WindowsSpyBlocker</td><td class="url-td td_text">https://raw.githubusercontent.com/crazy-max/WindowsSpyBlocker/master/data/hosts/spy.txt</td><td class="site-url-td td_text">https://github.com/crazy-max/WindowsSpyBlocker</td><td class="license-td td_text">MIT</td></tr>
<tr ><td class="category-td td_text">TrackingAndTelemetry</td><td class="name-td td_text">Easylist-easyprivacy</td><td class="url-td td_text">https://raw.githubusercontent.com/easylist/easylist/master/easyprivacy/easyprivacy_trackingservers.txt</td><td class="site-url-td td_text">https://easylist.to/</td><td class="license-td td_text">GPLv3</td></tr>
<tr ><td class="category-td td_text">TrackingAndTelemetry</td><td class="name-td td_text">louisa-uno-VRChatAnalyticsBlocklist</td><td class="url-td td_text">https://raw.githubusercontent.com/louisa-uno/VRChatAnalyticsBlocklist/master/hosts.txt</td><td class="site-url-td td_text">https://github.com/louisa-uno/VRChatAnalyticsBlocklist</td><td class="license-td td_text">AGPL</td></tr>
<tr ><td class="category-td td_text">Malicious</td><td class="name-td td_text">davidonzo-Threat-Intel</td><td class="url-td td_text">https://raw.githubusercontent.com/davidonzo/Threat-Intel/master/lists/latestdomains.txt</td><td class="site-url-td td_text">https://github.com/davidonzo/Threat-Intel</td><td class="license-td td_text">MIT</td></tr>
<tr ><td class="category-td td_text">Malicious</td><td class="name-td td_text">pishing.army-blocklist_extended</td><td class="url-td td_text">https://phishing.army/download/phishing_army_blocklist_extended.txt</td><td class="site-url-td td_text">https://phishing.army/</td><td class="license-td td_text">CC BY-NC 4.0</td></tr>
<tr ><td class="category-td td_text">Malicious</td><td class="name-td td_text">quidsup-notrack-blocklists-malware</td><td class="url-td td_text">https://gitlab.com/quidsup/notrack-blocklists/raw/master/notrack-malware.txt</td><td class="site-url-td td_text">https://gitlab.com/quidsup/notrack-blocklists</td><td class="license-td td_text">GPLv3</td></tr>
<tr ><td class="category-td td_text">Malicious</td><td class="name-td td_text">Spam404-lists</td><td class="url-td td_text">https://raw.githubusercontent.com/Spam404/lists/master/main-blacklist.txt</td><td class="site-url-td td_text">https://github.com/Spam404/lists</td><td class="license-td td_text">undefined</td></tr>
<tr ><td class="category-td td_text">Malicious</td><td class="name-td td_text">FadeMind-Risk</td><td class="url-td td_text">https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.Risk/hosts</td><td class="site-url-td td_text">http://hostsfile.org/hosts.html</td><td class="license-td td_text">GPLv3+</td></tr>
<tr ><td class="category-td td_text">Malicious</td><td class="name-td td_text">anudeepND-blacklist-CoinMiner</td><td class="url-td td_text">https://raw.githubusercontent.com/anudeepND/blacklist/master/CoinMiner.txt</td><td class="site-url-td td_text">https://github.com/anudeepND/blacklist</td><td class="license-td td_text">MIT</td></tr>
<tr ><td class="category-td td_text">Facebook</td><td class="name-td td_text">anudeepND-blacklist-facebook</td><td class="url-td td_text">https://raw.githubusercontent.com/anudeepND/blacklist/master/facebook.txt</td><td class="site-url-td td_text">https://github.com/anudeepND/blacklist</td><td class="license-td td_text">MIT</td></tr>
<tr ><td class="category-td td_text">Adult content</td><td class="name-td td_text">chadmayfield-my-pihole-blocklists</td><td class="url-td td_text">https://raw.githubusercontent.com/chadmayfield/my-pihole-blocklists/master/lists/pi_blocklist_porn_top1m.list</td><td class="site-url-td td_text">https://github.com/chadmayfield/my-pihole-blocklists</td><td class="license-td td_text">GPLv3</td></tr>
<tr ><td class="category-td td_text">Adult content</td><td class="name-td td_text">Easylist-easylist_adult</td><td class="url-td td_text">https://raw.githubusercontent.com/easylist/easylist/master/easylist_adult/adult_adservers.txt</td><td class="site-url-td td_text">https://easylist.to/</td><td class="license-td td_text">GPLv3</td></tr>
<tr ><td class="category-td td_text">TrackingAndTelemetry</td><td class="name-td td_text">hagezi-amazon</td><td class="url-td td_text">https://raw.githubusercontent.com/hagezi/dns-blocklists/main/domains/native.amazon.txt</td><td class="site-url-td td_text">undefined</td><td class="license-td td_text">GPLv3</td></tr>
<tr ><td class="category-td td_text">TrackingAndTelemetry</td><td class="name-td td_text">hagezi-apple</td><td class="url-td td_text">https://raw.githubusercontent.com/hagezi/dns-blocklists/main/domains/native.apple.txt</td><td class="site-url-td td_text">undefined</td><td class="license-td td_text">GPLv3</td></tr>
<tr ><td class="category-td td_text">TrackingAndTelemetry</td><td class="name-td td_text">hagezi-huawei</td><td class="url-td td_text">https://raw.githubusercontent.com/hagezi/dns-blocklists/main/domains/native.huawei.txt</td><td class="site-url-td td_text">undefined</td><td class="license-td td_text">GPLv3</td></tr>
<tr ><td class="category-td td_text">TrackingAndTelemetry</td><td class="name-td td_text">hagezi-lgwebos</td><td class="url-td td_text">https://raw.githubusercontent.com/hagezi/dns-blocklists/main/domains/native.lgwebos.txt</td><td class="site-url-td td_text">undefined</td><td class="license-td td_text">GPLv3</td></tr>
<tr ><td class="category-td td_text">TrackingAndTelemetry</td><td class="name-td td_text">hagezi-oppo-realme</td><td class="url-td td_text">https://raw.githubusercontent.com/hagezi/dns-blocklists/main/domains/native.oppo-realme.txt</td><td class="site-url-td td_text">undefined</td><td class="license-td td_text">GPLv3</td></tr>
<tr ><td class="category-td td_text">TrackingAndTelemetry</td><td class="name-td td_text">hagezi-tiktok-extended</td><td class="url-td td_text">https://raw.githubusercontent.com/hagezi/dns-blocklists/main/domains/native.tiktok.extended.txt</td><td class="site-url-td td_text">undefined</td><td class="license-td td_text">GPLv3</td></tr>
<tr ><td class="category-td td_text">TrackingAndTelemetry</td><td class="name-td td_text">hagezi-vivo</td><td class="url-td td_text">https://raw.githubusercontent.com/hagezi/dns-blocklists/main/domains/native.vivo.txt</td><td class="site-url-td td_text">undefined</td><td class="license-td td_text">GPLv3</td></tr>
<tr ><td class="category-td td_text">TrackingAndTelemetry</td><td class="name-td td_text">hagezi-winoffice</td><td class="url-td td_text">https://raw.githubusercontent.com/hagezi/dns-blocklists/main/domains/native.winoffice.txt</td><td class="site-url-td td_text">undefined</td><td class="license-td td_text">GPLv3</td></tr>
<tr ><td class="category-td td_text">TrackingAndTelemetry</td><td class="name-td td_text">hagezi-xiaomi</td><td class="url-td td_text">https://raw.githubusercontent.com/hagezi/dns-blocklists/main/domains/native.xiaomi.txt</td><td class="site-url-td td_text">undefined</td><td class="license-td td_text">GPLv3</td></tr>
<tr ><td class="category-td td_text">Mixed</td><td class="name-td td_text">hagezi-pro-plus</td><td class="url-td td_text">https://raw.githubusercontent.com/hagezi/dns-blocklists/main/domains/pro.plus.txt</td><td class="site-url-td td_text">undefined</td><td class="license-td td_text">GPLv3</td></tr>
<tr ><td class="category-td td_text">Mixed</td><td class="name-td td_text">osid-big</td><td class="url-td td_text">https://big.oisd.nl</td><td class="site-url-td td_text">undefined</td><td class="license-td td_text">GPLv3</td></tr>
<tr ><td class="category-td td_text">Adult content</td><td class="name-td td_text">osid-nsfw</td><td class="url-td td_text">https://nsfw.oisd.nl</td><td class="site-url-td td_text">undefined</td><td class="license-td td_text">GPLv3</td></tr></tbody></table>
<!-- MARKDOWN-AUTO-DOCS:END -->

## 🤝 Contributing

Whether a new list or improvement in the code or readme, we welcome contributions from you, this is how you can contribute to the project.

1. Fork the repository (<https://github.com/louisa-uno/DNSBlocklists>)
2. Commit your changes.
3. Push to the branch.
4. Create a new Pull Request.
