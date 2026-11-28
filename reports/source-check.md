# Source check — 2026-11-28

Checked 69 URLs: 0 unchanged, 0 changed, 31 broken, 4 empty, 34 new.

> This report only flags change. It does NOT update tuition /
> deadlines / visa thresholds. For every `changed` row, open the
> official URL, verify the figure on the page, then update the CSV
> / MD file by hand and bump its `last_verified` to today.

## Broken — check first

| Verdict | URL | Status | Note |
| --- | --- | --- | --- |
| broken | https://mfe.ieor.columbia.edu/ | 0 | HTTPSConnectionPool(host='mfe.ieor.columbia.edu', port=443): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x7f609c914550>: Failed to es |
| broken | https://mfe.baruch.cuny.edu/ | 0 | HTTPSConnectionPool(host='mfe.baruch.cuny.edu', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: |
| broken | https://math.nyu.edu/dynamic/masters/finmath/ | 404 | HTTP 404 |
| broken | https://msqf.nus.edu.sg/ | 0 | HTTPSConnectionPool(host='msqf.nus.edu.sg', port=443): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x7f609c914b90>: Failed to establis |
| broken | https://fmath.hkust.edu.hk/ | 0 | HTTPSConnectionPool(host='fmath.hkust.edu.hk', port=443): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x7f609c914e10>: Failed to estab |
| broken | https://cs.stanford.edu/academics/masters | 404 | HTTP 404 → redirected to https://www.cs.stanford.edu/academics/masters |
| broken | https://csd.cmu.edu/academics/masters | 404 | HTTP 404 |
| broken | https://www.cc.gatech.edu/degree-programs/master-science-computer-science | 0 | HTTPSConnectionPool(host='www.cc.gatech.edu', port=443): Max retries exceeded with url: /degree-programs/master-science-computer-science (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnect |
| broken | https://www.cst.cam.ac.uk/teaching/mphil | 404 | HTTP 404 |
| broken | https://mbzuai.ac.ae/study/ | 403 | HTTP 403 |
| broken | https://www.ece.cmu.edu/academics/ms-ece.html | 404 | HTTP 404 |
| broken | https://ee.stanford.edu/academics/masters | 404 | HTTP 404 |
| broken | https://www.ntu.edu.sg/eee/education/graduate | 404 | HTTP 404 |
| broken | https://me.stanford.edu/academics/graduate | 404 | HTTP 404 |
| broken | https://rsl.ethz.ch/studies/ | 404 | HTTP 404 |
| broken | https://www.imperial.ac.uk/mechanical-engineering/ | 0 | HTTPSConnectionPool(host='www.imperial.ac.uk', port=443): Max retries exceeded with url: /mechanical-engineering/ (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x7f609c9 |
| broken | https://www.ntu.edu.sg/mae/education/graduate | 404 | HTTP 404 |
| broken | https://www.datascience.columbia.edu/masters | 403 | HTTP 403 |
| broken | https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees | 403 | HTTP 403 |
| broken | https://msdsml.nus.edu.sg/ | 0 | HTTPSConnectionPool(host='msdsml.nus.edu.sg', port=443): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x7f609cc279d0>: Failed to establ |
| broken | https://msande.stanford.edu/academics/graduate-programs | 404 | HTTP 404 |
| broken | https://uwaterloo.ca/graduate-studies-postdoctoral-affairs/future-students/programs/business-entrepreneurship-and-technology-mbet | 404 | HTTP 404 |
| broken | https://www.ntu.edu.sg/ntc/education/graduate-programmes | 404 | HTTP 404 |
| broken | https://www.hec.edu/en/master-s-programs/specialized-master/msc-x-hec-entrepreneurs | 404 | HTTP 404 |
| broken | https://www.gov.uk/government/publications/innovator-visa-endorsing-bodies | 404 | HTTP 404 |
| broken | https://www.uscis.gov/working-in-the-united-states/temporary-workers/o-1-individuals-with-extraordinary-ability-or-achievement | 404 | HTTP 404 |
| broken | https://www.ice.gov/initiatives/stem-opt | 404 | HTTP 404 |
| broken | https://travel.state.gov/content/travel/en/us-visas/visa-information-resources/fees/treaty.html | 403 | HTTP 403 |
| broken | https://startupestonia.ee/visa/ | 404 | HTTP 404 |
| broken | https://ind.nl/en/residence-permits/work/startup | 404 | HTTP 404 |
| broken | https://vistos.mne.gov.pt | 0 | HTTPSConnectionPool(host='vistos.mne.gov.pt', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLError(1, '[SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:10 |

## Changed — verify on official page, then update CSV/MD

_(none)_

## Empty — page returned no text (JS shell or soft block); hash is not a baseline

| Verdict | URL | Status | Note |
| --- | --- | --- | --- |
| empty | https://www.imperial.ac.uk/business-school/ | 202 | hash e3b0c44298fc1c14 |
| empty | https://www.imperial.ac.uk/computing/ | 202 | hash e3b0c44298fc1c14 |
| empty | https://www.imperial.ac.uk/electrical-engineering/ | 202 | hash e3b0c44298fc1c14 |
| empty | https://www.imperial.ac.uk/business-school/programmes/ | 202 | hash e3b0c44298fc1c14 → redirected to https://www.imperial.ac.uk/business-school/study/ |

## New (first seen)

| Verdict | URL | Status | Note |
| --- | --- | --- | --- |
| new | https://bcf.princeton.edu/master-in-finance/ | 200 | hash 6e72504d37173edf → redirected to https://bcf.princeton.edu/academic-programs/master-in-finance/ |
| new | https://www.cmu.edu/mscf/ | 200 | hash 0d5d497d77b5df36 |
| new | https://mfe.haas.berkeley.edu/ | 200 | hash ab48a3a076a22103 |
| new | https://www.maths.ox.ac.uk/study-here/postgraduate-study/msc-mathematical-and-computational-finance | 200 | hash 47c5b1bee5818cb1 |
| new | https://cs.illinois.edu/academics/graduate | 200 | hash 51dcb42e5d8de9b6 → redirected to https://siebelschool.illinois.edu/academics/graduate |
| new | https://inf.ethz.ch/studies/master.html | 200 | hash 51038ab6179f1538 |
| new | https://www.comp.nus.edu.sg/programmes/pg/ | 200 | hash 8b114bf760fb04c7 → redirected to https://www.comp.nus.edu.sg/programmes/#graduate |
| new | https://prog-crs.hkust.edu.hk/pgprog/2026-27/msc-bdt | 200 | hash 9cb9fd5f8584770e |
| new | https://mscac.utoronto.ca/ | 200 | hash 5c09e8a07fe803c9 |
| new | https://admissions.kaust.edu.sa/ | 200 | hash 6c89b43883f66b3f |
| new | https://ece.illinois.edu/academics/grad | 200 | hash 2171010251aa87ce |
| new | https://prog-crs.hkust.edu.hk/pgprog/2026-27/msc-elec | 200 | hash c56250ab0f8addee |
| new | https://mrsd.ri.cmu.edu/ | 200 | hash 231aaa80bc337d10 |
| new | https://robotics.umich.edu/academics/graduate/ | 200 | hash 8f246dd02dd1d00c |
| new | https://datascience.uchicago.edu/education/masters/ | 200 | hash 5d50f217e6b78eef → redirected to https://datascience.uchicago.edu/education/masters-programs/masters-in-applied-ai/ |
| new | https://www.hec.edu/en/master-s-programs/ | 200 | hash c4895b74c0c51661 → redirected to https://www.hec.edu/en/master-s-programs |
| new | https://tpp.mit.edu/ | 200 | hash 8ee2787cc1e5c001 |
| new | https://www.gov.uk/innovator-founder-visa | 200 | hash 08f2d2ac50c90372 |
| new | https://www.gov.uk/graduate-visa | 200 | hash 07d9a6990ad820d5 |
| new | https://www.gov.uk/guidance/immigration-rules | 200 | hash efc7c2457a5325d7 |
| new | https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/start-visa.html | 200 | hash 03a7fde14b51f586 |
| new | https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/work/after-graduation.html | 200 | hash f10923bd1422effe |
| new | https://www.uscis.gov/i-941 | 200 | hash 5c2a3e7fdbcbba40 |
| new | https://www.uscis.gov/working-in-the-united-states/permanent-workers | 200 | hash 2dc653fd168b735b |
| new | https://www.uscis.gov/working-in-the-united-states/h-1b-specialty-occupations | 200 | hash 9761f19b3e60cd43 |
| new | https://www.mom.gov.sg/passes-and-permits/entrepass | 200 | hash 39e1b189e51bb3a9 |
| new | https://www.mom.gov.sg/passes-and-permits/entrepass/eligibility | 200 | hash 72066127fa6f88e2 |
| new | https://www.mom.gov.sg/passes-and-permits/overseas-networks-expertise-pass | 200 | hash e514207234902308 |
| new | https://www.enterprisesg.gov.sg/grow-your-business/innovate-with-us/innovation-talent/entrepass | 200 | hash a949f6569be5f982 |
| new | https://welcome.businessfrance.fr/en/french-tech-visa-for-founders | 200 | hash 68a83b67954b655e → redirected to https://welcome.businessfrance.fr/en/setting-up-a-business/recruiting-international-talent/visas-and-residence-permits/status-of-foreign-company-directors/french-tech-visa-for-founders/ |
| new | https://www.service-public.fr?recherche=passeport+talent+projet+economique+innovant | 200 | hash 4f1acd1d9629d1cc → redirected to https://www.service-public.gouv.fr/?recherche=passeport+talent+projet+economique+innovant |
| new | https://www.service-public.fr | 200 | hash 4f1acd1d9629d1cc → redirected to https://www.service-public.gouv.fr/ |
| new | https://icp.gov.ae | 200 | hash 3e120be76d5e821b → redirected to https://icp.gov.ae/ |
| new | https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/temporary-graduate-485 | 200 | hash b33ed0c88c3a556e |

## Unchanged

_(none)_
