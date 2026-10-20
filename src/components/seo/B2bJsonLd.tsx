import React from 'react';

export interface B2bSpecProperty {
  kbId?: string;
  name: string;
  value: string;
  conditions?: string;
}

export interface B2bFaqItem {
  question: string;
  answer: string;
}

export interface B2bJsonLdProps {
  companyName: string;
  companyUrl: string;
  pageUrl: string;
  pageTitle: string;
  pageDescription: string;
  inLanguage?: string;
  logoUrl?: string;
  sameAs?: string[];
  productName?: string;
  productSku?: string;
  productDescription?: string;
  material?: string;
  specs?: B2bSpecProperty[];
  faqs?: B2bFaqItem[];
}

export function B2bJsonLd({
  companyName,
  companyUrl,
  pageUrl,
  pageTitle,
  pageDescription,
  inLanguage = 'en',
  logoUrl,
  sameAs = [],
  productName,
  productSku,
  productDescription,
  material,
  specs = [],
  faqs = [],
}: B2bJsonLdProps) {
  const graph: Record<string, unknown>[] = [
    {
      '@type': 'Organization',
      '@id': `${companyUrl}#organization`,
      name: companyName,
      url: companyUrl,
      ...(logoUrl ? { logo: logoUrl } : {}),
      ...(sameAs.length > 0 ? { sameAs } : {}),
    },
    {
      '@type': 'WebSite',
      '@id': `${companyUrl}#website`,
      url: companyUrl,
      name: companyName,
      publisher: { '@id': `${companyUrl}#organization` },
    },
    {
      '@type': 'WebPage',
      '@id': `${pageUrl}#webpage`,
      url: pageUrl,
      name: pageTitle,
      description: pageDescription,
      inLanguage,
      publisher: { '@type': 'Organization', name: companyName, url: companyUrl },
    },
  ];

  if (productName && productDescription) {
    graph.push({
      '@type': 'Product',
      '@id': `${pageUrl}#product`,
      name: productName,
      description: productDescription,
      ...(productSku ? { sku: productSku } : {}),
      ...(material ? { material } : {}),
      brand: { '@type': 'Brand', name: companyName },
      manufacturer: { '@id': `${companyUrl}#organization` },
      ...(specs.length > 0
        ? {
            additionalProperty: specs.map((s) => ({
              '@type': 'PropertyValue',
              name: s.name,
              value: s.value,
              ...(s.conditions ? { description: s.conditions } : {}),
            })),
          }
        : {}),
    });
  }

  if (faqs.length > 0) {
    graph.push({
      '@type': 'FAQPage',
      '@id': `${pageUrl}#faq`,
      mainEntity: faqs.map((f) => ({
        '@type': 'Question',
        name: f.question,
        acceptedAnswer: {
          '@type': 'Answer',
          text: f.answer,
        },
      })),
    });
  }

  const payload = {
    '@context': 'https://schema.org',
    '@graph': graph,
  };

  return (
    <script
      type="application/ld+json"
      dangerouslySetInnerHTML={{ __html: JSON.stringify(payload) }}
    />
  );
}
