/*
 * DADOS DA PÁGINA — é aqui que você edita.
 *
 * Para cada certificação:
 *   udemy: link do simulado na Udemy. Se preencher, o card vira um botão "Simulado na Udemy"
 *          e já aparece primeiro na lista da plataforma.
 *   badge: link do badge no Credly (opcional). Usado quando não há link da Udemy.
 *   novo:  true para mostrar o selo "Novo".
 */
const PROFILE = {
  nome: 'Guilherme Benfica',
  linkedin: 'https://www.linkedin.com/in/guilherme-benfica',
  credly: 'https://www.credly.com/users/guilherme-benfica/badges#credly'
};

const PROVIDERS = [
  {
    id: 'aws',
    name: 'AWS',
    tagline: 'Golden Jacket 🧥',
    certs: [
      { code: 'CLF-C01', name: 'Cloud Practitioner', udemy: '', badge: '' },
      { code: 'AIF-C01', name: 'AI Practitioner', udemy: '', badge: '' },
      { code: 'DVA-C02', name: 'Developer Associate', udemy: '', badge: '' },
      { code: 'DEA-C01', name: 'Data Engineer Associate', udemy: '', badge: '' },
      { code: 'SAA-C03', name: 'Solutions Architect Associate', udemy: '', badge: '' },
      { code: 'SOA-C03', name: 'SysOps Administrator Associate', udemy: '', badge: '' },
      { code: 'MLA-C01', name: 'Machine Learning Engineer Associate', udemy: '', badge: '' },
      { code: 'SAP-C02', name: 'Solutions Architect Professional', udemy: '', badge: '' },
      { code: 'DOP-C01', name: 'DevOps Engineer Professional', udemy: '', badge: '' },
      { code: 'ANS-C01', name: 'Advanced Networking Specialty', udemy: '', badge: '' },
      { code: 'MLS-C01', name: 'Machine Learning Specialty', udemy: '', badge: '' },
      { code: 'AIP-C01', name: 'Generative AI Developer Professional', udemy: '', badge: '' },
      { code: 'SCS-C03', name: 'Security Specialty', udemy: '', badge: '' },
      { code: 'AB1-C01', name: 'Certificação AWS', udemy: '', badge: '' }
    ]
  },
  {
    id: 'azure',
    name: 'Microsoft Azure',
    tagline: 'Azure, IA e Power Platform',
    certs: [
      { code: 'AZ-900', name: 'Azure Fundamentals', udemy: '', badge: '' },
      { code: 'AI-900 / AI-901', name: 'Azure AI Fundamentals', udemy: '', badge: '' },
      { code: 'DP-900', name: 'Azure Data Fundamentals', udemy: '', badge: '' },
      { code: 'SC-900', name: 'Security, Compliance and Identity Fundamentals', udemy: '', badge: '' },
      { code: 'MS-900', name: 'Microsoft 365 Fundamentals', udemy: '', badge: '' },
      { code: 'PL-900', name: 'Power Platform Fundamentals', udemy: '', badge: '' },
      { code: 'AI-102 / AI-103', name: 'Azure AI Engineer Associate', udemy: '', badge: '' },
      { code: 'AZ-104', name: 'Azure Administrator Associate', udemy: '', badge: '' },
      { code: 'AZ-204 / AI-200', name: 'Azure Developer Associate', udemy: '', badge: '' },
      { code: 'AZ-500 / SC-500', name: 'Azure Security Engineer Associate', udemy: '', badge: '' },
      { code: 'DP-100', name: 'Azure Data Scientist Associate', udemy: '', badge: '' },
      { code: 'PL-300', name: 'Power BI Data Analyst Associate', udemy: '', badge: '' },
      { code: 'AZ-305', name: 'Azure Solutions Architect Expert', udemy: '', badge: '' }
    ]
  },
  {
    id: 'google',
    name: 'Google Cloud',
    tagline: 'Dados, nuvem e IA generativa',
    certs: [
      { code: 'CDL', name: 'Cloud Digital Leader', udemy: '', badge: '' },
      { code: 'GenAI Leader', name: 'Generative AI Leader', udemy: '', badge: '' },
      { code: 'ACE', name: 'Associate Cloud Engineer', udemy: '', badge: '' },
      { code: 'ADP', name: 'Associate Data Practitioner', udemy: '', badge: '' },
      { code: 'PDE', name: 'Professional Data Engineer', udemy: '', badge: '' },
      { code: 'PCDE', name: 'Professional Cloud Database Engineer', udemy: '', badge: '' }
    ]
  },
  {
    id: 'oracle',
    name: 'Oracle Cloud',
    tagline: 'OCI',
    certs: [
      { code: 'OCI AI', name: 'OCI AI Foundations Associate', udemy: '', badge: '' },
      { code: 'OCI', name: 'OCI Foundations Associate', udemy: '', badge: '' }
    ]
  },
  {
    id: 'github',
    name: 'GitHub',
    tagline: 'Copilot e IA agêntica',
    certs: [
      { code: 'GH-300', name: 'GitHub Copilot Certified', udemy: '', badge: '' },
      { code: 'GH-600', name: 'GitHub Agentic AI Developer', udemy: '', badge: '' }
    ]
  }
];
