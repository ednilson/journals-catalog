# coding: utf-8

#SciELO
scielo_columns_names = ['extraction_date',
 'study_unit',
 'collection',
 'issn_scielo',
 'issns',
 'title',
 'title_thematic_areas',
 'title_is_agricultural_sciences',
 'title_is_applied_social_sciences',
 'title_is_biological_sciences',
 'title_is_engineering',
 'title_is_exact_and_earth_sciences',
 'title_is_health_sciences',
 'title_is_human_sciences',
 'title_is_linguistics_letters_and_arts',
 'title_is_multidisciplinary',
 'title_current_status',
 'title_subtitle_scielo',
 'short_title_scielo',
 'short_title_iso',
 'title_pubmed',
 'publisher_name',
 'use_license',
 'alpha_frequency',
 'numeric_frequency_(in_months)',
 'inclusion_year_at_scielo',
 'stopping_year_at_scielo',
 'stopping_reason',
 'date_of_the_first_document',
 'volume_of_the_first_document',
 'issue_of_the_first_document',
 'date_of_the_last_document',
 'volume_of_the_last_document',
 'issue_of_the_last_document',
 'total_of_issues',
 'issues_at_2017',
 'issues_at_2016',
 'issues_at_2015',
 'issues_at_2014',
 'issues_at_2013',
 'issues_at_2012',
 'total_of_regular_issues',
 'regular_issues_at_2017',
 'regular_issues_at_2016',
 'regular_issues_at_2015',
 'regular_issues_at_2014',
 'regular_issues_at_2013',
 'regular_issues_at_2012',
 'total_of_documents',
 'documents_at_2017',
 'documents_at_2016',
 'documents_at_2015',
 'documents_at_2014',
 'documents_at_2013',
 'documents_at_2012',
 'citable_documents',
 'citable_documents_at_2017',
 'citable_documents_at_2016',
 'citable_documents_at_2015',
 'citable_documents_at_2014',
 'citable_documents_at_2013',
 'citable_documents_at_2012',
 'portuguese_documents_at_2017',
 'portuguese_documents_at_2016',
 'portuguese_documents_at_2015',
 'portuguese_documents_at_2014',
 'portuguese_documents_at_2013',
 'portuguese_documents_at_2012',
 'spanish_documents_at_2017',
 'spanish_documents_at_2016',
 'spanish_documents_at_2015',
 'spanish_documents_at_2014',
 'spanish_documents_at_2013',
 'spanish_documents_at_2012',
 'english_documents_at_2017',
 'english_documents_at_2016',
 'english_documents_at_2015',
 'english_documents_at_2014',
 'english_documents_at_2013',
 'english_documents_at_2012',
 'other_language_documents_at_2017',
 'other_language_documents_at_2016',
 'other_language_documents_at_2015',
 'other_language_documents_at_2014',
 'other_language_documents_at_2013',
 'other_language_documents_at_2012',
 'google_scholar_h5_2017',
 'google_scholar_h5_2016',
 'google_scholar_h5_2015',
 'google_scholar_h5_2014',
 'google_scholar_h5_2013',
 'google_scholar_h5_2012',
 'google_scholar_m5_2017',
 'google_scholar_m5_2016',
 'google_scholar_m5_2015',
 'google_scholar_m5_2014',
 'google_scholar_m5_2013',
 'google_scholar_m5_2012']

submission_scielo_brasil_columns_names = ['title',
 'data_inclusao_scielo',
 'issn_scielo',
 'scholarone',
 'ojs_scielo',
 'ojs_outro',
 'outro',
 'endereco_acesso']


# Scimago
scimagoall_columns_names = ['rank',
 'title',
 'type',
 'issn',
 'sjr',
 'sjr_best_quartile',
 'h_index',
 'total_docs',
 'total_docs_3years',
 'total_refs',
 'total_cites_3years',
 'citable_docs_3years',
 'cites_by_doc_2years',
 'ref_by_doc',
 'country']

scimago_columns_names_short = ['rank',
 'title',
 'type',
 'issn',
 'sjr',
 'sjr_best_quartile',
 'h_index',
 'total_doc_2015',
 'total_docs_3years',
 'total_refs',
 'total_cites_3years',
 'citable_docs_3years',
 'cites_by_doc_2years',
 'ref_bydoc',
 'country',
 'region',
 'year',
 'active']
 
scimago_columns_names = ['issn1',
 'issn2',
 'issn3',
 'title',
 'country',
 'region',
 'i1999_active',
 'i1999_sjr',
 'i1999_sjr_best_quartile',
 'i1999_h_index',
 'i1999_total_docs_2015',
 'i1999_total_docs_3years',
 'i1999_total_refs',
 'i1999_total_cites_3years',
 'i1999_citable_docs_3years',
 'i1999_cites_doc_2years',
 'i1999_ref_doc',
 'i2000_active',
 'i2000_sjr',
 'i2000_sjr_best_quartile',
 'i2000_h_index',
 'i2000_total_docs_2015',
 'i2000_total_docs_3years',
 'i2000_total_refs',
 'i2000_total_cites_3years',
 'i2000_citable_docs_3years',
 'i2000_cites_doc_2years',
 'i2000_ref_doc',
 'i2001_active',
 'i2001_sjr',
 'i2001_sjr_best_quartile',
 'i2001_h_index',
 'i2001_total_docs_2015',
 'i2001_total_docs_3years',
 'i2001_total_refs',
 'i2001_total_cites_3years',
 'i2001_citable_docs_3years',
 'i2001_cites_doc_2years',
 'i2001_ref_doc',
 'i2002_active',
 'i2002_sjr',
 'i2002_sjr_best_quartile',
 'i2002_h_index',
 'i2002_total_docs_2015',
 'i2002_total_docs_3years',
 'i2002_total_refs',
 'i2002_total_cites_3years',
 'i2002_citable_docs_3years',
 'i2002_cites_doc_2years',
 'i2002_ref_doc',
 'i2003_active',
 'i2003_sjr',
 'i2003_sjr_best_quartile',
 'i2003_h_index',
 'i2003_total_docs_2015',
 'i2003_total_docs_3years',
 'i2003_total_refs',
 'i2003_total_cites_3years',
 'i2003_citable_docs_3years',
 'i2003_cites_doc_2years',
 'i2003_ref_doc',
 'i2004_active',
 'i2004_sjr',
 'i2004_sjr_best_quartile',
 'i2004_h_index',
 'i2004_total_docs_2015',
 'i2004_total_docs_3years',
 'i2004_total_refs',
 'i2004_total_cites_3years',
 'i2004_citable_docs_3years',
 'i2004_cites_doc_2years',
 'i2004_ref_doc',
 'i2005_active',
 'i2005_sjr',
 'i2005_sjr_best_quartile',
 'i2005_h_index',
 'i2005_total_docs_2015',
 'i2005_total_docs_3years',
 'i2005_total_refs',
 'i2005_total_cites_3years',
 'i2005_citable_docs_3years',
 'i2005_cites_doc_2years',
 'i2005_ref_doc',
 'i2006_active',
 'i2006_sjr',
 'i2006_sjr_best_quartile',
 'i2006_h_index',
 'i2006_total_docs_2015',
 'i2006_total_docs_3years',
 'i2006_total_refs',
 'i2006_total_cites_3years',
 'i2006_citable_docs_3years',
 'i2006_cites_doc_2years',
 'i2006_ref_doc',
 'i2007_active',
 'i2007_sjr',
 'i2007_sjr_best_quartile',
 'i2007_h_index',
 'i2007_total_docs_2015',
 'i2007_total_docs_3years',
 'i2007_total_refs',
 'i2007_total_cites_3years',
 'i2007_citable_docs_3years',
 'i2007_cites_doc_2years',
 'i2007_ref_doc',
 'i2008_active',
 'i2008_sjr',
 'i2008_sjr_best_quartile',
 'i2008_h_index',
 'i2008_total_docs_2015',
 'i2008_total_docs_3years',
 'i2008_total_refs',
 'i2008_total_cites_3years',
 'i2008_citable_docs_3years',
 'i2008_cites_doc_2years',
 'i2008_ref_doc',
 'i2009_active',
 'i2009_sjr',
 'i2009_sjr_best_quartile',
 'i2009_h_index',
 'i2009_total_docs_2015',
 'i2009_total_docs_3years',
 'i2009_total_refs',
 'i2009_total_cites_3years',
 'i2009_citable_docs_3years',
 'i2009_cites_doc_2years',
 'i2009_ref_doc',
 'i2010_active',
 'i2010_sjr',
 'i2010_sjr_best_quartile',
 'i2010_h_index',
 'i2010_total_docs_2015',
 'i2010_total_docs_3years',
 'i2010_total_refs',
 'i2010_total_cites_3years',
 'i2010_citable_docs_3years',
 'i2010_cites_doc_2years',
 'i2010_ref_doc',
 'i2011_active',
 'i2011_sjr',
 'i2011_sjr_best_quartile',
 'i2011_h_index',
 'i2011_total_docs_2015',
 'i2011_total_docs_3years',
 'i2011_total_refs',
 'i2011_total_cites_3years',
 'i2011_citable_docs_3years',
 'i2011_cites_doc_2years',
 'i2011_ref_doc',
 'i2012_active',
 'i2012_sjr',
 'i2012_sjr_best_quartile',
 'i2012_h_index',
 'i2012_total_docs_2015',
 'i2012_total_docs_3years',
 'i2012_total_refs',
 'i2012_total_cites_3years',
 'i2012_citable_docs_3years',
 'i2012_cites_doc_2years',
 'i2012_ref_doc',
 'i2013_active',
 'i2013_sjr',
 'i2013_sjr_best_quartile',
 'i2013_h_index',
 'i2013_total_docs_2015',
 'i2013_total_docs_3years',
 'i2013_total_refs',
 'i2013_total_cites_3years',
 'i2013_citable_docs_3years',
 'i2013_cites_doc_2years',
 'i2013_ref_doc',
 'i2014_active',
 'i2014_sjr',
 'i2014_sjr_best_quartile',
 'i2014_h_index',
 'i2014_total_docs_2015',
 'i2014_total_docs_3years',
 'i2014_total_refs',
 'i2014_total_cites_3years',
 'i2014_citable_docs_3years',
 'i2014_cites_doc_2years',
 'i2014_ref_doc',
 'i2015_active',
 'i2015_sjr',
 'i2015_sjr_best_quartile',
 'i2015_h_index',
 'i2015_total_docs_2015',
 'i2015_total_docs_3years',
 'i2015_total_refs',
 'i2015_total_cites_3years',
 'i2015_citable_docs_3years',
 'i2015_cites_doc_2years',
 'i2015_ref_doc']


# Scopus
scopus_columns_names_2015 = ['sourcerecord_id',
 'title',
 'print_issn',
 'e_issn',
 'active_or_inactive',
 'coverage',
 'article_language_source_iso_codes',
 'citescore_2013',
 'sjr_2013',
 'snip_2013',
 'citescore_2014',
 'sjr_2014',
 'snip_2014',
 'citescore_2015',
 'sjr_2015',
 'snip_2015',
 'medline_sourced_title',
 'open_acces_status',
 'articles_in_press_included',
 'added_to_list_since_october_2016',
 'source_type',
 'title_history_indication',
 'related_title_to_title_history_indication',
 'other_related_title_1',
 'other_related_title_2',
 'other_related_title_3',
 'publishers_name',
 'publisher_imprints_grouped_to_main_publisher',
 'publishers_country',
 'all_science_classification_codes_asjc',
 'top_level_life_sciences',
 'top_level_social_sciences',
 'top_level_physical_sciences',
 'top_level_health_sciences',
 'c1000_general',
 'c1100_agricultural_and_biological_sciences',
 'c1200_arts_and_humanities',
 'c1300_biochemistry_genetics_and_molecular_biology',
 'c1400_business_management_and_accounting',
 'c1500_chemical_engineering',
 'c1600_chemistry',
 'c1700_computer_science',
 'c1800_decision_sciences',
 'c1900_earth_and_planetary_sciences',
 'c2000_economics_econometrics_and_finance',
 'c2100_energy',
 'c2200_engineering',
 'c2300_environmental_science',
 'c2400_immunology_and_microbiology',
 'c2500_materials_science',
 'c2600_mathematics',
 'c2700_medicine',
 'c2800_neuroscience',
 'c2900_nursing',
 'c3000_pharmacology_toxicology_and_pharmaceutics',
 'c3100_physics_and_astronomy',
 'c3200_psychology',
 'c3300_social_sciences',
 'c3400_veterinary',
 'c3500_dentistry',
 'c3600_health_professions']

scopus_columns_names_2016 = ['sourcerecord_id',
 'title',
 'print_issn',
 'e_issn',
 'active_or_inactive',
 'coverage',
 'article_language_source_iso_codes',
 'citescore_2014', 
 'sjr_2014',
 'snip_2014',
 'citescore_2015',
 'sjr_2015',
 'snip_2015',
 'citescore_2016', # new indicators to 2016
 'sjr_2016',
 'snip_2016',
 'medline_sourced_title',
 'open_acces_status',
 'articles_in_press_included',
 'added_to_list_since_october_2016',
 'source_type',
 'title_history_indication',
 'related_title_to_title_history_indication',
 'other_related_title_1',
 'other_related_title_2',
 'other_related_title_3',
 'publishers_name',
 'publisher_imprints_grouped_to_main_publisher',
 'publishers_country',
 'all_science_classification_codes_asjc',
 'top_level_life_sciences',
 'top_level_social_sciences',
 'top_level_physical_sciences',
 'top_level_health_sciences',
 'c1000_general',
 'c1100_agricultural_and_biological_sciences',
 'c1200_arts_and_humanities',
 'c1300_biochemistry_genetics_and_molecular_biology',
 'c1400_business_management_and_accounting',
 'c1500_chemical_engineering',
 'c1600_chemistry',
 'c1700_computer_science',
 'c1800_decision_sciences',
 'c1900_earth_and_planetary_sciences',
 'c2000_economics_econometrics_and_finance',
 'c2100_energy',
 'c2200_engineering',
 'c2300_environmental_science',
 'c2400_immunology_and_microbiology',
 'c2500_materials_science',
 'c2600_mathematics',
 'c2700_medicine',
 'c2800_neuroscience',
 'c2900_nursing',
 'c3000_pharmacology_toxicology_and_pharmaceutics',
 'c3100_physics_and_astronomy',
 'c3200_psychology',
 'c3300_social_sciences',
 'c3400_veterinary',
 'c3500_dentistry',
 'c3600_health_professions']


scopuscitscore_columns_names = ['scopus_sourceid',
 'title',
 'citescore',
 'percentile',
 'citation_count',
 'scholarly_output',
 'percent_cited',
 'snip',
 'sjr',
 'rank',
 'rank_out_of',
 'publisher',
 'type',
 'openaccess',
 'scopus_asjc_code_(sub-subject_area)',
 'scopus_sub-subject_area',
 'quartile',
 'top_10_(citescore_percentile)',
 'url',
 'print_issn',
 'eissn']


# WOS
wos_columns_names = ['rank',
 'title',
 'jcr_abbreviated_title',
 'issn',
 'total_cites',
 'journal_impact_factor',
 'impact_factor_without_journal_self_cites',
 'five_year_impact_factor',
 'immediacy_index',
 'citable_items',
 'cited_half_life',
 'citing_half_life',
 'eigenfactor_score',
 'article_influence_score',
 'percentage_articles_in_citable_items',
 'empty',
 'average_journal_impact_factor_percentile',
 'normalized_eigenfactor']


#CWTS
cwts_columns_names = ['title_and_country_scimago',
 'title',
 'print_issn',
 'electronic_issn',
 'asjc_field_ids',
 'i1999_citing_source',
 'i1999_p',
 'i1999_ipp',
 'i1999_ipp_lower_bound',
 'i1999_ipp_upper_bound',
 'i1999_snip',
 'i1999_snip_lower_bound',
 'i1999_snip_upper_bound',
 'i1999_perc_self_cit',
 'i1999_active',
 'i2000_citing_source',
 'i2000_p',
 'i2000_ipp',
 'i2000_ipp_lower_bound',
 'i2000_ipp_upper_bound',
 'i2000_snip',
 'i2000_snip_lower_bound',
 'i2000_snip_upper_bound',
 'i2000_perc_self_cit',
 'i2000_active',
 'i2001_citing_source',
 'i2001_p',
 'i2001_ipp',
 'i2001_ipp_lower_bound',
 'i2001_ipp_upper_bound',
 'i2001_snip',
 'i2001_snip_lower_bound',
 'i2001_snip_upper_bound',
 'i2001_perc_self_cit',
 'i2001_active',
 'i2002_citing_source',
 'i2002_p',
 'i2002_ipp',
 'i2002_ipp_lower_bound',
 'i2002_ipp_upper_bound',
 'i2002_snip',
 'i2002_snip_lower_bound',
 'i2002_snip_upper_bound',
 'i2002_perc_self_cit',
 'i2002_active',
 'i2003_citing_source',
 'i2003_p',
 'i2003_ipp',
 'i2003_ipp_lower_bound',
 'i2003_ipp_upper_bound',
 'i2003_snip',
 'i2003_snip_lower_bound',
 'i2003_snip_upper_bound',
 'i2003_perc_self_cit',
 'i2003_active',
 'i2004_citing_source',
 'i2004_p',
 'i2004_ipp',
 'i2004_ipp_lower_bound',
 'i2004_ipp_upper_bound',
 'i2004_snip',
 'i2004_snip_lower_bound',
 'i2004_snip_upper_bound',
 'i2004_perc_self_cit',
 'i2004_active',
 'i2005_citing_source',
 'i2005_p',
 'i2005_ipp',
 'i2005_ipp_lower_bound',
 'i2005_ipp_upper_bound',
 'i2005_snip',
 'i2005_snip_lower_bound',
 'i2005_snip_upper_bound',
 'i2005_perc_self_cit',
 'i2005_active',
 'i2006_citing_source',
 'i2006_p',
 'i2006_ipp',
 'i2006_ipp_lower_bound',
 'i2006_ipp_upper_bound',
 'i2006_snip',
 'i2006_snip_lower_bound',
 'i2006_snip_upper_bound',
 'i2006_perc_self_cit',
 'i2006_active',
 'i2007_citing_source',
 'i2007_p',
 'i2007_ipp',
 'i2007_ipp_lower_bound',
 'i2007_ipp_upper_bound',
 'i2007_snip',
 'i2007_snip_lower_bound',
 'i2007_snip_upper_bound',
 'i2007_perc_self_cit',
 'i2007_active',
 'i2008_citing_source',
 'i2008_p',
 'i2008_ipp',
 'i2008_ipp_lower_bound',
 'i2008_ipp_upper_bound',
 'i2008_snip',
 'i2008_snip_lower_bound',
 'i2008_snip_upper_bound',
 'i2008_perc_self_cit',
 'i2008_active',
 'i2009_citing_source',
 'i2009_p',
 'i2009_ipp',
 'i2009_ipp_lower_bound',
 'i2009_ipp_upper_bound',
 'i2009_snip',
 'i2009_snip_lower_bound',
 'i2009_snip_upper_bound',
 'i2009_perc_self_cit',
 'i2009_active',
 'i2010_citing_source',
 'i2010_p',
 'i2010_ipp',
 'i2010_ipp_lower_bound',
 'i2010_ipp_upper_bound',
 'i2010_snip',
 'i2010_snip_lower_bound',
 'i2010_snip_upper_bound',
 'i2010_perc_self_cit',
 'i2010_active',
 'i2011_citing_source',
 'i2011_p',
 'i2011_ipp',
 'i2011_ipp_lower_bound',
 'i2011_ipp_upper_bound',
 'i2011_snip',
 'i2011_snip_lower_bound',
 'i2011_snip_upper_bound',
 'i2011_perc_self_cit',
 'i2011_active',
 'i2012_citing_source',
 'i2012_p',
 'i2012_ipp',
 'i2012_ipp_lower_bound',
 'i2012_ipp_upper_bound',
 'i2012_snip',
 'i2012_snip_lower_bound',
 'i2012_snip_upper_bound',
 'i2012_perc_self_cit',
 'i2012_active',
 'i2013_citing_source',
 'i2013_p',
 'i2013_ipp',
 'i2013_ipp_lower_bound',
 'i2013_ipp_upper_bound',
 'i2013_snip',
 'i2013_snip_lower_bound',
 'i2013_snip_upper_bound',
 'i2013_perc_self_cit',
 'i2013_active',
 'i2014_citing_source',
 'i2014_p',
 'i2014_ipp',
 'i2014_ipp_lower_bound',
 'i2014_ipp_upper_bound',
 'i2014_snip',
 'i2014_snip_lower_bound',
 'i2014_snip_upper_bound',
 'i2014_perc_self_cit',
 'i2014_active',
 'i2015_citing_source',
 'i2015_p',
 'i2015_ipp',
 'i2015_ipp_lower_bound',
 'i2015_ipp_upper_bound',
 'i2015_snip',
 'i2015_snip_lower_bound',
 'i2015_snip_upper_bound',
 'i2015_perc_self_cit',
 'i2015_active']


doaj_columns_names = ['colecao',
 'title',
 'issn',
 'link_doaj',
 'ultimo_ano_no_doaj',
 'licenca_no_doaj',
 'licenca_scielo',
 'disponivel_doaj',
 'atualizado_no_doaj',
 'data_de_conferencia',
 'plataforma',
 'selo_doaj',
 'ti_envia_dados',
 'enviado_formulario_pelo_editor',
 'data_de_confirmacao_de_envio',
 'observacoes']


capes_columns_names = ['issn', 
'title', 
'area_avaliacao', 
'estrato']
