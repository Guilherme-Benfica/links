"""Gera index.html (português) e en/index.html (inglês) a partir dos dados abaixo.

Para editar textos ou links: altere COURSES / TEXT e rode  python3 tools/build_pages.py
"""
import html
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://guilherme-benfica.github.io/links/"
VERSION = "13"  # aumente quando mudar style.css ou as imagens (evita cache antigo)

PROFILE = {
    "name": "Guilherme Benfica",
    "linkedin": "https://www.linkedin.com/in/guilherme-benfica/",
    "credly": "https://www.credly.com/users/guilherme-benfica/badges#credly",
    "builder": "https://builder.aws.com/community/@guilhermebenfica?tab=articles",
}

# Imagem de compartilhamento: a página principal usa a versão bilíngue (aparece no LinkedIn para todo mundo)
# O nome muda (v2, v3...) quando a imagem muda, porque LinkedIn e WhatsApp guardam a imagem antiga em cache
OG_IMAGE = {"pt": "og-bilingue-v2.jpg", "en": "og-en-v2.jpg"}

# Ordem = jornada sugerida (do primeiro passo até Professional)
# "q" = questões por simulado (são 5 simulados por curso).
# Curso que existe só em um idioma: deixe a chave do outro idioma fora de "url" (e de "coupon").
# Quando publicar a versão em português, é só acrescentar "pt" em "url" e "coupon".
COURSES = [
    {
        "id": "clf", "q": 65, "code": "CLF-C02", "name": "Cloud Practitioner", "full": "AWS Certified Cloud Practitioner",
        "level": {"pt": "Foundational", "en": "Foundational"},
        "tag": {"pt": "Ideal para começar", "en": "Best place to start"},
        "desc": {"pt": "Sua primeira certificação AWS: conceitos de nuvem, segurança, serviços principais, preços e suporte.",
                 "en": "Your first AWS certification: cloud concepts, security, core services, pricing, and support."},
        "coupon": {"pt": "AWSGRATIS2026", "en": "AWSFREE2026"},  # cupom gratuito (deixe "" para tirar)
        "url": {"pt": "https://www.udemy.com/course/simulados-aws-cloud-practitioner-clf-c02-atualizado/?referralCode=EC24E96FDD556E35A0CD",
                "en": "https://www.udemy.com/course/aws-cloud-practitioner-practice-exams-clf-c02-updated/?referralCode=2849BD6DE0A1EBC83FCE"},
    },
    {
        "id": "aif", "q": 65, "code": "AIF-C01", "name": "AI Practitioner", "full": "AWS Certified AI Practitioner",
        "level": {"pt": "Foundational", "en": "Foundational"},
        "tag": {"pt": "Não exige programação", "en": "No coding required"},
        "desc": {"pt": "Fundamentos de IA e ML, IA generativa, agentes, Amazon Bedrock e IA responsável.",
                 "en": "AI and ML fundamentals, generative AI, agents, Amazon Bedrock, and responsible AI."},
        "coupon": {"pt": "AWSFREE", "en": "AWSFREE2026"},  # cupom gratuito (deixe "" para tirar)
        "url": {"pt": "https://www.udemy.com/course/simulados-aws-ai-practitioner-aif-c01-atualizado/?referralCode=81BEE17F71273E8EC291",
                "en": "https://www.udemy.com/course/aws-ai-practitioner-practice-exams-aif-c01/?referralCode=43233F7D54E7BBA1B47E"},
    },
    {
        "id": "aib", "q": 65, "code": "AIB-C01", "name": "AI Business Strategist", "full": "AWS Certified AI Business Strategist",
        "level": {"pt": "Business", "en": "Business"},
        "tag": {"pt": "Para liderança e negócios", "en": "For business and leadership"},
        "desc": {"pt": "Estratégia de IA, valor para o negócio, governança e liderança de iniciativas de IA.",
                 "en": "AI strategy, business value, governance, and leading AI initiatives."},
        "coupon": {"pt": "AWSFREE", "en": "AWSFREE"},  # cupom gratuito (deixe "" para tirar)
        "url": {"pt": "https://www.udemy.com/course/simulados-aws-ai-business-strategist-aib-c01/?referralCode=FE9480FFEC3ACC4BABCC",
                "en": "https://www.udemy.com/course/aws-ai-business-strategist-practice-exams-aib-c01/?referralCode=9FB0C7D2A84E522D44F3"},
    },
    {
        "id": "saa", "q": 65, "code": "SAA-C03", "name": "Solutions Architect", "full": "AWS Certified Solutions Architect - Associate",
        "level": {"pt": "Associate", "en": "Associate"},
        "tag": {"pt": "Atualizado para o SAA-C03", "en": "Updated for SAA-C03"},
        "desc": {"pt": "Arquiteturas seguras, resilientes, de alto desempenho e com custo otimizado na AWS.",
                 "en": "Secure, resilient, high-performing, and cost-optimized architectures on AWS."},
        "coupon": {"pt": "AWSNOVFREE", "en": "AWSNOVFREE"},  # cupom gratuito (deixe "" para tirar)
        "url": {"pt": "https://www.udemy.com/course/simulados-aws-solutions-architect-associate-saa-c03/",
                "en": "https://www.udemy.com/course/aws-solutions-architect-associate-practice-exams-saa-c03/"},
    },
    {
        "id": "soa", "q": 65, "code": "SOA-C03", "name": "CloudOps Engineer", "full": "AWS Certified CloudOps Engineer - Associate",
        "level": {"pt": "Associate", "en": "Associate"},
        "tag": {"pt": "Operações na nuvem", "en": "Cloud operations"},
        "desc": {"pt": "Monitoramento, confiabilidade, implantação, automação, segurança e redes na operação de workloads na AWS.",
                 "en": "Monitoring, reliability, deployment, automation, security, and networking for operating AWS workloads."},
        "coupon": {"en": "AWSNOVFREE"},  # só em inglês por enquanto
        "url": {"en": "https://www.udemy.com/course/aws-cloudops-engineer-associate-practice-exams-soa-c03/"},
    },
    {
        "id": "dea", "q": 65, "code": "DEA-C01", "name": "Data Engineer", "full": "AWS Certified Data Engineer - Associate",
        "level": {"pt": "Associate", "en": "Associate"},
        "tag": {"pt": "Engenharia de dados", "en": "Data engineering"},
        "desc": {"pt": "Ingestão e transformação de dados, armazenamento, operações, segurança e governança de dados.",
                 "en": "Data ingestion and transformation, storage, operations, security, and data governance."},
        "coupon": {"en": "AWSNOVFREE"},  # só em inglês por enquanto
        "url": {"en": "https://www.udemy.com/course/aws-data-engineer-associate-exams-dea-c01/"},
    },
    {
        "id": "mla", "q": 65, "code": "MLA-C02", "name": "Machine Learning Engineer", "full": "AWS Certified Machine Learning Engineer - Associate",
        "level": {"pt": "Associate", "en": "Associate"},
        "tag": {"pt": "Atualizado para o MLA-C02", "en": "Updated for MLA-C02"},
        "desc": {"pt": "Preparação de dados, modelos, implantação, MLOps e IA generativa com SageMaker AI e Amazon Bedrock.",
                 "en": "Data preparation, models, deployment, MLOps, and generative AI with SageMaker AI and Amazon Bedrock."},
        "coupon": {"pt": "AWSFREE", "en": "AWSFREE"},  # cupom gratuito (deixe "" para tirar)
        "url": {"pt": "https://www.udemy.com/course/simulados-aws-machine-learning-engineer-mla-c02/?referralCode=425ACC388C26A359F7CD",
                "en": "https://www.udemy.com/course/aws-machine-learning-engineer-practice-exams-mla-c02/?referralCode=CFB4C2B61A3481D5FB71"},
    },
    {
        "id": "aip", "q": 75, "code": "AIP-C01", "name": "Generative AI Developer", "full": "AWS Certified Generative AI Developer - Professional",
        "level": {"pt": "Professional", "en": "Professional"},
        "tag": {"pt": "IA generativa para desenvolvedores", "en": "Generative AI for developers"},
        "desc": {"pt": "Soluções de IA generativa em produção: modelos de fundação, RAG, agentes, segurança e governança.",
                 "en": "Generative AI solutions in production: foundation models, RAG, agents, security, and governance."},
        "coupon": {"en": "AWSNOVFREE"},  # só em inglês por enquanto
        "url": {"en": "https://www.udemy.com/course/aws-generative-ai-developer-pro-aip-c01-practice-exams/"},
    },
]

TEXT = {
    "pt": {
        "html_lang": "pt-BR", "og_locale": "pt_BR", "path": "", "prefix": "",
        "title": "Simulados AWS | SAA-C03, SOA-C03, DEA-C01, AIP-C01 e mais",
        "description": "Simulados AWS com todas as respostas comentadas para CLF-C02, AIF-C01, AIB-C01, SAA-C03, SOA-C03, DEA-C01, MLA-C02 e AIP-C01. 5 provas por curso, feitas por um AWS Golden Jacket.",
        "skip": "Pular para os simulados",
        "lang_label": "Idioma", "lang_pt": "Português", "lang_en": "English",
        "eyebrow": "AWS Golden Jacket · todas as certificações AWS ativas",
        "h1": "Simulados AWS com <em>todas as respostas</em> comentadas",
        "lede": "Questões escritas a partir do guia oficial de cada exame, no formato e no tempo da prova. Em cada uma, você entende por que a certa está certa e por que as outras estão erradas.",
        "cta": "Escolher meu simulado",
        "stat_labels": ("certificações", "simulados completos", "questões comentadas"), "thousands": ".",
        "courses_kicker": "Simulados na Udemy",
        "courses_h2": "Escolha sua certificação",
        "courses_note": "Os cursos com botão PT / EN têm versão nos dois idiomas. Os demais estão em inglês.",
        "course_lang_label": "Idioma do simulado",
        "btn_by_lang": {"pt": "Ver simulado na Udemy", "en": "Ver simulado em inglês na Udemy"},
        "aria_by_lang": {"pt": "Abrir o simulado {code} {name} em português na Udemy", "en": "Abrir o simulado {code} {name} em inglês na Udemy"},
        "meta": "5 simulados · {q} questões cada", "meta_only": {"en": " · em inglês"},
        "button": "Ver simulado na Udemy",
        "aria_button": "Abrir o simulado {code} {name} na Udemy",
        "benefits_h2": "O que você encontra em cada curso",
        "benefits": [
            ("Todas as alternativas explicadas", "Por que a certa está certa e por que cada uma das outras está errada."),
            ("Um exemplo prático por questão", "Cada explicação traz um cenário real para fixar o conceito."),
            ("No ritmo da prova", "Simulados cronometrados, com o número de questões do exame."),
            ("Guiado pelo exame oficial", "Domínios e pesos do guia oficial de cada certificação."),
        ],
        "author_kicker": "Quem escreveu",
        "author_h2": "Feito por quem passou por todas",
        "author_p": "Sou Guilherme Benfica, AWS Golden Jacket: tenho todas as certificações AWS ativas. Cada uma exigiu meses de preparação, e foi assim que aprendi o que realmente decide a prova: interpretar o cenário, e não decorar respostas. Esses simulados reúnem essa experiência.",
        "author_links": [("linkedin", "Conectar no LinkedIn"), ("builder", "Ler meus artigos sobre AWS"), ("credly", "Ver minhas certificações no Credly")],
        "footer_links": [("linkedin", "LinkedIn"), ("builder", "Artigos AWS"), ("credly", "Credly")],
        "faq_h2": "Perguntas frequentes",
        "lang_all": "Sim. Todos os cursos têm uma versão em português e outra em inglês, com as mesmas questões e explicações. É só escolher PT ou EN no card.",
        "lang_some": "Depende do curso. {both} têm uma versão em português e outra em inglês, com as mesmas questões e explicações: é só escolher PT ou EN no card. {only} estão disponíveis em inglês.",
        "and": " e ",
        "faq": [
            ("Os simulados são em português?", "{lang_answer}"),
            ("Qual simulado devo fazer primeiro?", "Comece pelo seu objetivo: nuvem em geral (CLF-C02), IA sem programação (AIF-C01 e AIB-C01), arquitetura (SAA-C03), operações (SOA-C03), dados (DEA-C01), machine learning (MLA-C02) ou IA generativa para desenvolvedores (AIP-C01). Quem está começando na AWS pode partir do CLF-C02."),
            ("As questões são as mesmas da prova real?", "Não. São questões originais, escritas a partir do guia oficial de cada exame para treinar o mesmo tipo de raciocínio que a prova cobra."),
            ("Preciso saber programar?", "Para o CLF-C02, o AIF-C01 e o AIB-C01, não. Os demais são de nível Associate ou Professional e esperam experiência prática com a AWS. O DEA-C01 pede familiaridade com pipelines de dados, e o MLA-C02 e o AIP-C01, com machine learning e desenvolvimento de IA."),
            ("O link do card já aplica o cupom?", "Sim. O link de cada card já leva o cupom promocional. Cupons da Udemy têm prazo e limite de usos: se o preço aparecer cheio, o cupom já expirou."),
            ("Por quanto tempo tenho acesso?", "Na Udemy, o acesso ao curso é vitalício e inclui as atualizações dos simulados."),
        ],
        "hint": "This page is also available in English.",
        "hint_link": "View in English",
        "hint_close": "Fechar",
        "disclaimer": "Cursos independentes, sem afiliação com a Amazon Web Services. AWS e os nomes das certificações são marcas da Amazon.com, Inc. ou de suas afiliadas.",
        "img_alt": "Capa do curso de simulados {full} ({code})",
        "photo_alt": "Foto de Guilherme Benfica",
        "list_name": "Simulados AWS de Guilherme Benfica",
    },
    "en": {
        "html_lang": "en", "og_locale": "en_US", "path": "en/", "prefix": "../",
        "title": "AWS Practice Exams | SAA-C03, SOA-C03, DEA-C01, AIP-C01 and more",
        "description": "AWS practice exams with every answer explained for CLF-C02, AIF-C01, AIB-C01, SAA-C03, SOA-C03, DEA-C01, MLA-C02, and AIP-C01. 5 full exams per course, by an AWS Golden Jacket.",
        "skip": "Skip to the practice exams",
        "lang_label": "Language", "lang_pt": "Português", "lang_en": "English",
        "eyebrow": "AWS Golden Jacket · every active AWS certification",
        "h1": "AWS practice exams with <em>every answer</em> explained",
        "lede": "Questions written from each official exam guide, in the format and at the pace of the real exam. For each one, you learn why the right answer is right and why the others are wrong.",
        "cta": "Choose my practice exam",
        "stat_labels": ("certifications", "full practice exams", "explained questions"), "thousands": ",",
        "courses_kicker": "Practice exams on Udemy",
        "courses_h2": "Choose your certification",
        "courses_note": "Courses with a PT / EN switch come in both languages. The others are in English.",
        "course_lang_label": "Practice exam language",
        "btn_by_lang": {"en": "View practice exams on Udemy", "pt": "View the Portuguese version on Udemy"},
        "aria_by_lang": {"en": "Open the {code} {name} practice exams in English on Udemy", "pt": "Open the {code} {name} practice exams in Portuguese on Udemy"},
        "meta": "5 exams · {q} questions each", "meta_only": {"pt": " · in Portuguese"},
        "button": "View practice exams on Udemy",
        "aria_button": "Open the {code} {name} practice exams on Udemy",
        "benefits_h2": "What you get in every course",
        "benefits": [
            ("Every option explained", "Why the right answer is right and why each of the others is wrong."),
            ("A practical example per question", "Each explanation includes a real scenario to lock in the concept."),
            ("At the real exam's pace", "Timed exams with the same number of questions as the real test."),
            ("Built on the official exam", "Domains and weights from each certification's official guide."),
        ],
        "author_kicker": "Who wrote them",
        "author_h2": "Built by someone who passed them all",
        "author_p": "I'm Guilherme Benfica, an AWS Golden Jacket: I hold every active AWS certification. Each one took months of preparation, and that taught me what really decides the exam: reading the scenario, not memorizing answers. These practice exams bring that experience together.",
        "author_links": [("linkedin", "Connect on LinkedIn"), ("builder", "Read my AWS articles"), ("credly", "See my certifications on Credly")],
        "footer_links": [("linkedin", "LinkedIn"), ("builder", "AWS articles"), ("credly", "Credly")],
        "faq_h2": "Frequently asked questions",
        "lang_all": "Yes. Every course has an English and a Portuguese version, with the same questions and explanations. Just pick PT or EN on the card.",
        "lang_some": "It depends on the course. {both} come in English and Portuguese, with the same questions and explanations: just pick PT or EN on the card. {only} are available in English.",
        "and": ", and ",
        "faq": [
            ("Are the practice exams available in Portuguese?", "{lang_answer}"),
            ("Which practice exam should I take first?", "Start from your goal: general cloud (CLF-C02), AI without coding (AIF-C01 and AIB-C01), architecture (SAA-C03), operations (SOA-C03), data (DEA-C01), machine learning (MLA-C02), or generative AI for developers (AIP-C01). If you are new to AWS, CLF-C02 is a good first step."),
            ("Are these the real exam questions?", "No. They are original questions written from each official exam guide, to train the same kind of reasoning the exam tests."),
            ("Do I need to know how to code?", "Not for CLF-C02, AIF-C01, or AIB-C01. The others are Associate or Professional level and expect hands-on AWS experience. DEA-C01 expects familiarity with data pipelines, and MLA-C02 and AIP-C01 expect familiarity with machine learning and AI development."),
            ("Does the card link already apply the coupon?", "Yes. Each card link already carries the promotional coupon. Udemy coupons have an expiry date and a limited number of uses: if the full price shows up, the coupon has expired."),
            ("How long do I have access?", "On Udemy, course access is lifetime and includes updates to the practice exams."),
        ],
        "hint": "Esta página também está disponível em português.",
        "hint_link": "Ver em português",
        "hint_close": "Close",
        "disclaimer": "Independent courses, not affiliated with Amazon Web Services. AWS and the certification names are trademarks of Amazon.com, Inc. or its affiliates.",
        "img_alt": "Course cover for the {full} ({code}) practice exams",
        "photo_alt": "Photo of Guilherme Benfica",
        "list_name": "AWS practice exams by Guilherme Benfica",
    },
}

ICONS = [
    '<path d="M9 12l2 2 4-4"/><circle cx="12" cy="12" r="9"/>',
    '<path d="M9 18h6"/><path d="M10 21h4"/><path d="M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2.1h5c0-.9.4-1.6 1-2.1A6 6 0 0 0 12 3z"/>',
    '<circle cx="12" cy="13" r="8"/><path d="M12 9v4l2.5 2.5"/><path d="M9 2h6"/>',
    '<path d="M4 4h16v16H4z"/><path d="M4 9h16"/><path d="M9 9v11"/>',
]

LINK_ICONS = {
    "linkedin": '<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4.4 3.6-7 8-7s8 2.6 8 7"/>',
    "builder": '<path d="M6 3h9l4 4v14H6z"/><path d="M14 3v5h5"/><path d="M9 13h7"/><path d="M9 17h5"/>',
    "credly": '<circle cx="12" cy="9" r="6"/><path d="M8.5 14l-1.5 7 5-3 5 3-1.5-7"/>',
}

e = html.escape


def course_link(c, lang):
    """Link da Udemy com o código de indicação e, se houver, o cupom gratuito."""
    url = c["url"][lang]
    code = c.get("coupon", {}).get(lang)
    if not code:
        return url
    return f"{url}{'&' if '?' in url else '?'}couponCode={code}"


def join_codes(codes, t):
    """'A, B e C' (pt) ou 'A, B, and C' (en)."""
    if len(codes) == 1:
        return codes[0]
    return ", ".join(codes[:-1]) + t["and"] + codes[-1]


def faq_list(t):
    both = [c["code"] for c in COURSES if len(c["url"]) == 2]
    only = [c["code"] for c in COURSES if len(c["url"]) == 1]
    ans = t["lang_some"].format(both=join_codes(both, t), only=join_codes(only, t)) if only else t["lang_all"]
    return [(q, a.replace("{lang_answer}", ans)) for q, a in t["faq"]]


def eff_lang(c, lang):
    """Idioma que o card mostra: o da página, ou o único que o curso tem."""
    return lang if lang in c["url"] else next(iter(c["url"]))


def fmt_num(n, sep):
    return f"{n:,}".replace(",", sep)


def clean_url(c, lang):
    return c["url"][lang].split("?")[0]


def jsonld(lang, t):
    url = SITE + t["path"]
    person = {"@type": "Person", "@id": SITE + "#guilherme", "name": PROFILE["name"],
              "description": "AWS Golden Jacket", "image": SITE + "img/foto.webp",
              "sameAs": [PROFILE["linkedin"], PROFILE["credly"], PROFILE["builder"]]}
    items = [{"@type": "ListItem", "position": i + 1, "item": {
        "@type": "Course", "name": f'{c["full"]} ({c["code"]})', "description": c["desc"][lang],
        "url": clean_url(c, eff_lang(c, lang)), "inLanguage": TEXT[eff_lang(c, lang)]["html_lang"], "image": SITE + f'img/{c["id"]}-{eff_lang(c, lang)}.webp',
        "provider": {"@type": "Organization", "name": "Udemy", "sameAs": "https://www.udemy.com"},
        "creator": {"@id": SITE + "#guilherme"}}} for i, c in enumerate(COURSES)]
    graph = [
        {"@type": "WebPage", "@id": url, "url": url, "name": t["title"], "description": t["description"],
         "inLanguage": t["html_lang"], "author": {"@id": SITE + "#guilherme"}, "primaryImageOfPage": SITE + f"img/{OG_IMAGE[lang]}"},
        person,
        {"@type": "ItemList", "name": t["list_name"], "itemListElement": items},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq_list(t)]},
    ]
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)


def page(lang):
    t = TEXT[lang]
    p = t["prefix"]
    other = "en" if lang == "pt" else "pt"
    other_href = p + TEXT[other]["path"] if lang == "en" else TEXT[other]["path"]
    if lang == "en":
        other_href = "../"
    url = SITE + t["path"]
    v = VERSION

    def lang_link(code):
        here = code == lang
        href = ("./" if here else other_href)
        label = t["lang_pt"] if code == "pt" else t["lang_en"]
        hl = "pt-BR" if code == "pt" else "en"
        cur = ' aria-current="page"' if here else ""
        return f'<a href="{href}" hreflang="{hl}" lang="{hl}"{cur}><span class="lang-code">{code.upper()}</span><span class="lang-name">{label}</span></a>'

    n_courses = len(COURSES)
    stat_values = (str(n_courses), str(5 * n_courses), fmt_num(sum(5 * c["q"] for c in COURSES), t["thousands"]))
    stats = "".join(f'<li><strong>{e(n)}</strong><span>{e(l)}</span></li>' for n, l in zip(stat_values, t["stat_labels"]))
    cards = []
    for i, c in enumerate(COURSES):
        el = eff_lang(c, lang)            # idioma do card nesta página
        both = len(c["url"]) == 2          # só mostra o botão PT / EN se o curso existe nos dois
        loading = 'fetchpriority="high"' if i < 2 else 'loading="lazy"'
        alt = e(t["img_alt"].format(full=c["full"], code=c["code"]))
        data = " ".join(
            f'data-href-{l}="{e(course_link(c, l))}" data-img-{l}="{p}img/{c["id"]}-{l}.webp?v={v}" '
            f'data-btn-{l}="{e(t["btn_by_lang"][l])}" data-aria-{l}="{e(t["aria_by_lang"][l].format(code=c["code"], name=c["name"]))}"'
            for l in ("pt", "en")) if both else ""
        meta = t["meta"].format(q=c["q"]) + ("" if both else t["meta_only"].get(el, ""))
        toggle = "".join(
            f'<button type="button" data-set="{l}" lang="{"pt-BR" if l == "pt" else "en"}" aria-pressed="{"true" if l == lang else "false"}">{l.upper()}</button>'
            for l in ("pt", "en")) if both else ""
        cards.append(f'''
      <li class="card c-{c["id"]} lv-{c["level"]["en"].lower()}"{" " + data if data else ""}>
        <div class="card-media"><img src="{p}img/{c["id"]}-{el}.webp?v={v}" width="750" height="422" {loading} decoding="async" alt="{alt}"></div>
        <div class="card-body">
          <div class="card-meta"><span class="code">{c["code"]}</span><span class="level">{c["level"][lang]}</span></div>
          <h3><a href="{e(course_link(c, el))}" target="_blank" rel="noopener" aria-label="{e(t["aria_by_lang"][el].format(code=c["code"], name=c["name"]))}">{c["name"]}</a></h3>
          <p class="tag">{e(c["tag"][lang])}</p>
          <p class="desc">{e(c["desc"][lang])}</p>
          <div class="facts-row">
            <p class="facts">{e(meta)}</p>
            {f'<div class="clang" role="group" aria-label="{e(t["course_lang_label"])}" hidden>{toggle}</div>' if both else ""}
          </div>
          <span class="btn" aria-hidden="true"><span class="btn-label">{e(t["btn_by_lang"][el])}</span> <svg viewBox="0 0 24 24"><path d="M7 17L17 7"/><path d="M8 7h9v9"/></svg></span>
        </div>
      </li>''')
    benefits = "".join(f'''
        <li><svg class="ico" viewBox="0 0 24 24" aria-hidden="true">{ICONS[i]}</svg><h3>{e(h)}</h3><p>{e(d)}</p></li>'''
                       for i, (h, d) in enumerate(t["benefits"]))
    faq = "".join(f'''
        <details><summary>{e(q)}</summary><p>{e(a)}</p></details>''' for q, a in faq_list(t))

    return f'''<!DOCTYPE html>
<html lang="{t["html_lang"]}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="Content-Security-Policy" content="default-src 'none'; script-src 'self'; style-src 'self'; img-src 'self' data:; font-src 'self'; base-uri 'self'; form-action 'none'; object-src 'none'; upgrade-insecure-requests">
  <meta name="referrer" content="strict-origin-when-cross-origin">
  <title>{e(t["title"])}</title>
  <meta name="description" content="{e(t["description"])}">
  <meta name="author" content="{PROFILE["name"]}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="{url}">
  <link rel="alternate" hreflang="pt-BR" href="{SITE}">
  <link rel="alternate" hreflang="en" href="{SITE}en/">
  <link rel="alternate" hreflang="x-default" href="{SITE}">
  <meta name="theme-color" content="#070b16">
  <link rel="icon" href="{p}favicon.svg" type="image/svg+xml">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{PROFILE["name"]}">
  <meta property="og:locale" content="{t["og_locale"]}">
  <meta property="og:locale:alternate" content="{TEXT[other]["og_locale"]}">
  <meta property="og:title" content="{e(t["title"])}">
  <meta property="og:description" content="{e(t["description"])}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{SITE}img/{OG_IMAGE[lang]}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{e(t["title"])}">
  <meta name="twitter:description" content="{e(t["description"])}">
  <meta name="twitter:image" content="{SITE}img/{OG_IMAGE[lang]}">
  <link rel="preload" href="{p}fonts/bricolage-grotesque-latin-800-normal.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="{p}fonts/instrument-sans-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="{p}style.css?v={v}">
  <script type="application/ld+json">
{jsonld(lang, t)}
  </script>
</head>
<body>
  <a class="skip" href="#simulados">{e(t["skip"])}</a>

  <div class="hint" id="hint" hidden data-lang="{lang}">
    <span lang="{TEXT[other]["html_lang"]}">{e(t["hint"])}</span>
    <a href="{other_href}" hreflang="{TEXT[other]["html_lang"]}" lang="{TEXT[other]["html_lang"]}">{e(t["hint_link"])} &rarr;</a>
    <button type="button" id="hint-close" aria-label="{e(t["hint_close"])}">&times;</button>
  </div>

  <header class="topbar">
    <a class="brand" href="./"><span class="hex" aria-hidden="true"></span>{PROFILE["name"]}</a>
    <nav class="lang" aria-label="{e(t["lang_label"])}">{lang_link("pt")}{lang_link("en")}</nav>
  </header>

  <main>
    <section class="hero">
      <div class="hero-photo"><img src="{p}img/foto.webp?v={v}" width="240" height="240" alt="{e(t["photo_alt"])}"></div>
      <p class="eyebrow">{e(t["eyebrow"])}</p>
      <h1>{t["h1"]}</h1>
      <p class="lede">{e(t["lede"])}</p>
      <a class="cta" href="#simulados">{e(t["cta"])} <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 5v14"/><path d="M6 13l6 6 6-6"/></svg></a>
      <ul class="stats">{stats}</ul>
      <ul class="badges" aria-hidden="true">{"".join(f'<li><img src="{p}img/badge-{c["id"]}.webp?v={v}" width="240" height="240" alt="" loading="lazy"></li>' for c in COURSES)}</ul>
    </section>

    <section class="courses" id="simulados" aria-labelledby="courses-h">
      <p class="kicker">{e(t["courses_kicker"])}</p>
      <h2 id="courses-h">{e(t["courses_h2"])}</h2>
      <ul class="grid">{"".join(cards)}
      </ul>
      <p class="switch-note">{e(t["courses_note"])}</p>
    </section>

    <section class="benefits" aria-labelledby="benefits-h">
      <h2 id="benefits-h">{e(t["benefits_h2"])}</h2>
      <ul>{benefits}
      </ul>
    </section>

    <section class="author" aria-labelledby="author-h">
      <img src="{p}img/foto.webp?v={v}" width="240" height="240" alt="" loading="lazy">
      <div>
        <p class="kicker">{e(t["author_kicker"])}</p>
        <h2 id="author-h">{e(t["author_h2"])}</h2>
        <p>{e(t["author_p"])}</p>
        <ul class="author-links">{"".join(f'<li><a class="pill-link" href="{PROFILE[k]}" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" aria-hidden="true">{LINK_ICONS[k]}</svg>{e(label)}</a></li>' for k, label in t["author_links"])}</ul>
      </div>
    </section>

    <section class="faq" aria-labelledby="faq-h">
      <h2 id="faq-h">{e(t["faq_h2"])}</h2>{faq}
    </section>
  </main>

  <footer>
    <nav class="social" aria-label="Links">
      {"".join(f'<a href="{PROFILE[k]}" target="_blank" rel="noopener">{e(label)}</a>' for k, label in t["footer_links"])}
    </nav>
    <p>{e(t["disclaimer"])}</p>
    <p>&copy; 2026 {PROFILE["name"]}</p>
  </footer>

  <script src="{p}site.js?v={v}" defer></script>
</body>
</html>
'''


SITEMAP = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url>
    <loc>{SITE}</loc>
    <xhtml:link rel="alternate" hreflang="pt-BR" href="{SITE}"/>
    <xhtml:link rel="alternate" hreflang="en" href="{SITE}en/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{SITE}"/>
  </url>
  <url>
    <loc>{SITE}en/</loc>
    <xhtml:link rel="alternate" hreflang="pt-BR" href="{SITE}"/>
    <xhtml:link rel="alternate" hreflang="en" href="{SITE}en/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{SITE}"/>
  </url>
</urlset>
'''

if __name__ == "__main__":
    (ROOT / "index.html").write_text(page("pt"), encoding="utf-8")
    (ROOT / "en").mkdir(exist_ok=True)
    (ROOT / "en" / "index.html").write_text(page("en"), encoding="utf-8")
    (ROOT / "sitemap.xml").write_text(SITEMAP, encoding="utf-8")
    print("ok: index.html, en/index.html, sitemap.xml")
