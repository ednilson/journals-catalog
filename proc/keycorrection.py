# coding: utf-8

#SciELO

scielo_collection_name = {      
    u'arg': u'Argentina',      
    u'bol': u'Bolivia',        
    u'chl': u'Chile',      
    u'col': u'Colombia',       
    u'cri': u'Costa Rica',     
    u'cub': u'Cuba',       
    u'esp': u'Spain',      
    u'mex': u'Mexico',     
    u'per': u'Peru',       
    u'prt': u'Portugal',       
    u'scl': u'Brazil',     
    u'spa': u'Public Health',      
    u'sss': u'Social Sciences',        
    u'sza': u'South Africa',       
    u'ury': u'Uruguay',        
    u'ven': u'Venezuela',            
}


scielo_columns_names = ['extraction_date',
 'study_unit',
 'collection',
 'issn_scielo',
 'issns',
 'title_at_scielo',
 'title_thematic_areas',
 'title_is_agricultural_sciences',
 'title_is_applied_social_sciences',
 'title_is_biological_sciences',
 'title_is_engineering',
 'title_is_exact_and_earth_sciences',
 'title_is_health_sciences',
 'title_is_human_sciences',
 'title_is_linguistics,_letters_and_arts',
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


# Scimago

scimago_columns_names = ['rank',
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
 

 # Scopus
 
scopus_columns_names = ['sourcerecord_id',
 'source_title',
 'print_issn',
 'e_issn',
 'coverage',
 'active_or_inactive',
 '2013_citescore',
 '2013_sjr',
 '2013_snip',
 '2014_citescore',
 '2014_sjr',
 '2014_snip',
 '2015_citescore',
 '2015_sjr',
 '2015_snip',
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
 '1000_general',
 '1100_agricultural_and_biological_sciences',
 '1200_arts_and_humanities',
 '1300_biochemistry_genetics_and_molecular_biology',
 '1400_business_management_and_accounting',
 '1500_chemical_engineering',
 '1600_chemistry',
 '1700_computer_science',
 '1800_decision_sciences',
 '1900_earth_and_planetary_sciences',
 '2000_economics_econometrics_and_finance',
 '2100_energy',
 '2200_engineering',
 '2300_environmental_science',
 '2400_immunology_and_microbiology',
 '2500_materials_science',
 '2600_mathematics',
 '2700_medicine',
 '2800_neuroscience',
 '2900_nursing',
 '3000_pharmacology_toxicology_and_pharmaceutics',
 '3100_physics_and_astronomy',
 '3200_psychology',
 '3300_social_sciences',
 '3400_veterinary',
 '3500_dentistry',
 '3600_health_professions']


# JCR

jcr_columns_names = ['rank',
 'full_journal_title',
 'jcr_abbreviated_title',
 'issn',
 'total_cites',
 'journal_impact_factor',
 'impact_factor_without_journal_self_cites',
 '5year_impact_factor',
 'immediacy_index',
 'citable_items',
 'cited_half-life',
 'citing_half-life',
 'eigenfactor_score',
 'article_influence_score',
 'percentage_articles_in_citable_items',
 'empty',
 'average_journal_impact_factor_percentile',
 'normalized_eigenfactor']

 #CWTS
cwts_columns_names = ['title_and_country_scimago',
 'source_title',
 'print_issn',
 'electronic_issn',
 'asjc_field_ids',
 '1999_citing_source',
 '1999_p',
 '1999_ipp',
 '1999_ipp_lower_bound',
 '1999_ipp_upper_bound',
 '1999_snip',
 '1999_snip_lower_bound',
 '1999_snip_upper_bound',
 '1999_perc_self_cit',
 '1999_active',
 '2000_citing_source',
 '2000_p',
 '2000_ipp',
 '2000_ipp_lower_bound',
 '2000_ipp_upper_bound',
 '2000_snip',
 '2000_snip_lower_bound',
 '2000_snip_upper_bound',
 '2000_perc_self_cit',
 '2000_active',
 '2001_citing_source',
 '2001_p',
 '2001_ipp',
 '2001_ipp_lower_bound',
 '2001_ipp_upper_bound',
 '2001_snip',
 '2001_snip_lower_bound',
 '2001_snip_upper_bound',
 '2001_perc_self_cit',
 '2001_active',
 '2002_citing_source',
 '2002_p',
 '2002_ipp',
 '2002_ipp_lower_bound',
 '2002_ipp_upper_bound',
 '2002_snip',
 '2002_snip_lower_bound',
 '2002_snip_upper_bound',
 '2002_perc_self_cit',
 '2002_active',
 '2003_citing_source',
 '2003_p',
 '2003_ipp',
 '2003_ipp_lower_bound',
 '2003_ipp_upper_bound',
 '2003_snip',
 '2003_snip_lower_bound',
 '2003_snip_upper_bound',
 '2003_perc_self_cit',
 '2003_active',
 '2004_citing_source',
 '2004_p',
 '2004_ipp',
 '2004_ipp_lower_bound',
 '2004_ipp_upper_bound',
 '2004_snip',
 '2004_snip_lower_bound',
 '2004_snip_upper_bound',
 '2004_perc_self_cit',
 '2004_active',
 '2005_citing_source',
 '2005_p',
 '2005_ipp',
 '2005_ipp_lower_bound',
 '2005_ipp_upper_bound',
 '2005_snip',
 '2005_snip_lower_bound',
 '2005_snip_upper_bound',
 '2005_perc_self_cit',
 '2005_active',
 '2006_citing_source',
 '2006_p',
 '2006_ipp',
 '2006_ipp_lower_bound',
 '2006_ipp_upper_bound',
 '2006_snip',
 '2006_snip_lower_bound',
 '2006_snip_upper_bound',
 '2006_perc_self_cit',
 '2006_active',
 '2007_citing_source',
 '2007_p',
 '2007_ipp',
 '2007_ipp_lower_bound',
 '2007_ipp_upper_bound',
 '2007_snip',
 '2007_snip_lower_bound',
 '2007_snip_upper_bound',
 '2007_perc_self_cit',
 '2007_active',
 '2008_citing_source',
 '2008_p',
 '2008_ipp',
 '2008_ipp_lower_bound',
 '2008_ipp_upper_bound',
 '2008_snip',
 '2008_snip_lower_bound',
 '2008_snip_upper_bound',
 '2008_perc_self_cit',
 '2008_active',
 '2009_citing_source',
 '2009_p',
 '2009_ipp',
 '2009_ipp_lower_bound',
 '2009_ipp_upper_bound',
 '2009_snip',
 '2009_snip_lower_bound',
 '2009_snip_upper_bound',
 '2009_perc_self_cit',
 '2009_active',
 '2010_citing_source',
 '2010_p',
 '2010_ipp',
 '2010_ipp_lower_bound',
 '2010_ipp_upper_bound',
 '2010_snip',
 '2010_snip_lower_bound',
 '2010_snip_upper_bound',
 '2010_perc_self_cit',
 '2010_active',
 '2011_citing_source',
 '2011_p',
 '2011_ipp',
 '2011_ipp_lower_bound',
 '2011_ipp_upper_bound',
 '2011_snip',
 '2011_snip_lower_bound',
 '2011_snip_upper_bound',
 '2011_perc_self_cit',
 '2011_active',
 '2012_citing_source',
 '2012_p',
 '2012_ipp',
 '2012_ipp_lower_bound',
 '2012_ipp_upper_bound',
 '2012_snip',
 '2012_snip_lower_bound',
 '2012_snip_upper_bound',
 '2012_perc_self_cit',
 '2012_active',
 '2013_citing_source',
 '2013_p',
 '2013_ipp',
 '2013_ipp_lower_bound',
 '2013_ipp_upper_bound',
 '2013_snip',
 '2013_snip_lower_bound',
 '2013_snip_upper_bound',
 '2013_perc_self_cit',
 '2013_active',
 '2014_citing_source',
 '2014_p',
 '2014_ipp',
 '2014_ipp_lower_bound',
 '2014_ipp_upper_bound',
 '2014_snip',
 '2014_snip_lower_bound',
 '2014_snip_upper_bound',
 '2014_perc_self_cit',
 '2014_active',
 '2015_citing_source',
 '2015_p',
 '2015_ipp',
 '2015_ipp_lower_bound',
 '2015_ipp_upper_bound',
 '2015_snip',
 '2015_snip_lower_bound',
 '2015_snip_upper_bound',
 '2015_perc_self_cit',
 '2015_active']