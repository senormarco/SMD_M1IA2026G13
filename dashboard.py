#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
MODULE 8 — Dashboard Marketing interactif
Objectif : visualisation interactive des KPI, de la segmentation
client, de la performance marketing et des ventes.

Lancement :
    pip install streamlit pandas matplotlib plotly

    streamlit run dashboard.py
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# =============================================================================
# CONFIGURATION
# =============================================================================

st.set_page_config(
    page_title="Dashboard Marketing IA",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded"
)


# =============================================================================
# CHEMINS
# =============================================================================

DATA_DIR = "data"
OUT_DIR = "outputs"


# =============================================================================
# STYLE PROFESSIONNEL
# =============================================================================

st.markdown(
    """
    <style>

    /* --------------------------------------------------------------------- */
    /* GLOBAL                                                               */
    /* --------------------------------------------------------------------- */

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1500px;
    }

    h1, h2, h3 {
        letter-spacing: -0.02em;
    }

    /* --------------------------------------------------------------------- */
    /* KPI CARDS                                                            */
    /* --------------------------------------------------------------------- */

    div[data-testid="stMetric"] {
        background: rgba(128, 128, 128, 0.06);
        border: 1px solid rgba(128, 128, 128, 0.18);
        border-radius: 10px;
        padding: 18px 20px;
        min-height: 120px;
    }

    div[data-testid="stMetricLabel"] {
        font-size: 0.85rem;
        font-weight: 600;
    }

    div[data-testid="stMetricValue"] {
        font-size: 1.65rem;
        font-weight: 700;
    }

    /* --------------------------------------------------------------------- */
    /* SIDEBAR                                                              */
    /* --------------------------------------------------------------------- */

    section[data-testid="stSidebar"] {
        border-right: 1px solid rgba(128, 128, 128, 0.15);
    }

    section[data-testid="stSidebar"] h1 {
        font-size: 1.35rem;
    }

    /* --------------------------------------------------------------------- */
    /* INFO BOX                                                             */
    /* --------------------------------------------------------------------- */

    .info-box {
        padding: 16px 18px;
        border-radius: 8px;
        background-color: rgba(33, 150, 243, 0.06);
        border-left: 4px solid #2196F3;
        margin: 12px 0;
        line-height: 1.6;
    }

    /* --------------------------------------------------------------------- */
    /* SUCCESS BOX                                                          */
    /* --------------------------------------------------------------------- */

    .success-box {
        padding: 16px 18px;
        border-radius: 8px;
        background-color: rgba(76, 175, 80, 0.06);
        border-left: 4px solid #4CAF50;
        margin: 12px 0;
        line-height: 1.6;
    }

    /* --------------------------------------------------------------------- */
    /* WARNING BOX                                                          */
    /* --------------------------------------------------------------------- */

    .warning-box {
        padding: 16px 18px;
        border-radius: 8px;
        background-color: rgba(255, 193, 7, 0.07);
        border-left: 4px solid #FFC107;
        margin: 12px 0;
        line-height: 1.6;
    }

    /* --------------------------------------------------------------------- */
    /* FIGURE CAPTION                                                       */
    /* --------------------------------------------------------------------- */

    .figure-caption {
        font-size: 0.88rem;
        color: #666;
        line-height: 1.55;
        margin-top: 4px;
        margin-bottom: 18px;
    }

    .figure-title {
        font-weight: 700;
        font-size: 1rem;
        margin-bottom: 4px;
    }

    /* --------------------------------------------------------------------- */
    /* SECTION HEADER                                                       */
    /* --------------------------------------------------------------------- */

    .section-description {
        color: #666;
        line-height: 1.65;
        margin-bottom: 1rem;
    }

    /* --------------------------------------------------------------------- */
    /* FOOTER                                                               */
    /* --------------------------------------------------------------------- */

    .footer {
        text-align: center;
        color: #777;
        font-size: 0.82rem;
        padding: 20px 0;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =============================================================================
# CHARGEMENT DES DONNÉES
# =============================================================================

@st.cache_data
def load_data():

    customers = pd.read_csv(
        f"{DATA_DIR}/customers_data.csv"
    )

    sales = pd.read_csv(
        f"{DATA_DIR}/sales_data_.csv"
    )

    products = pd.read_csv(
        f"{DATA_DIR}/products_data.csv"
    )

    marketing = pd.read_csv(
        f"{DATA_DIR}/marketing_data.csv"
    )

    # -------------------------------------------------------------------------
    # CALCUL DU REVENU
    # -------------------------------------------------------------------------

    sales["Revenue"] = (
        sales["Quantity"] * sales["Sale_Price"]
    )

    # -------------------------------------------------------------------------
    # CTR
    # -------------------------------------------------------------------------

    marketing["CTR (%)"] = (
        marketing["Clicks"]
        .div(
            marketing["Impressions"].replace(0, pd.NA)
        )
        .mul(100)
        .fillna(0)
        .round(2)
    )

    # -------------------------------------------------------------------------
    # TAUX DE CONVERSION
    # -------------------------------------------------------------------------

    marketing["Taux_Conversion (%)"] = (
        marketing["Conversions"]
        .div(
            marketing["Clicks"].replace(0, pd.NA)
        )
        .mul(100)
        .fillna(0)
        .round(2)
    )

    # -------------------------------------------------------------------------
    # CPA
    # -------------------------------------------------------------------------

    marketing["CPA (€)"] = (
        marketing["Budget"]
        .div(
            marketing["Conversions"].replace(0, pd.NA)
        )
        .fillna(0)
        .round(2)
    )

    # -------------------------------------------------------------------------
    # ROI
    # -------------------------------------------------------------------------

    revenu_moyen = sales["Revenue"].mean()

    marketing["ROI (%)"] = (
        (
            marketing["Conversions"] * revenu_moyen
            - marketing["Budget"]
        )
        .div(
            marketing["Budget"].replace(0, pd.NA)
        )
        .mul(100)
        .fillna(0)
        .round(1)
    )

    # -------------------------------------------------------------------------
    # SEGMENTATION
    # -------------------------------------------------------------------------

    try:

        segmented = pd.read_csv(
            f"{OUT_DIR}/customers_segmented.csv"
        )

    except FileNotFoundError:

        segmented = None

    # -------------------------------------------------------------------------
    # PERSONAS
    # -------------------------------------------------------------------------

    try:

        personas = pd.read_csv(
            f"{OUT_DIR}/personas.csv"
        )

    except FileNotFoundError:

        personas = None

    return (
        customers,
        sales,
        products,
        marketing,
        segmented,
        personas
    )


# =============================================================================
# CHARGEMENT
# =============================================================================

try:

    (
        customers,
        sales,
        products,
        marketing,
        segmented,
        personas
    ) = load_data()

except FileNotFoundError as error:

    st.error(
        "Impossible de charger les fichiers de données."
    )

    st.code(str(error))

    st.info(
        "Vérifiez que les fichiers CSV sont présents "
        "dans le dossier data/."
    )

    st.stop()


# =============================================================================
# SIDEBAR
# =============================================================================

with st.sidebar:

    st.title("Marketing IA")

    st.caption(
        "Tableau de bord d'analyse marketing"
    )

    st.divider()

    st.subheader("Sources de données")

    st.write(
        f"Clients : **{len(customers):,}**"
    )

    st.write(
        f"Ventes : **{len(sales):,}**"
    )

    st.write(
        f"Produits : **{len(products):,}**"
    )

    st.write(
        f"Campagnes : **{len(marketing):,}**"
    )

    st.divider()

    st.subheader("Définitions des indicateurs")

    with st.expander("CTR"):

        st.write(
            "Le CTR mesure la proportion d'impressions "
            "ayant généré un clic."
        )

        st.latex(
            r"CTR = \frac{Clicks}{Impressions} \times 100"
        )

    with st.expander("Taux de conversion"):

        st.write(
            "Le taux de conversion mesure la proportion "
            "de clics transformés en conversions."
        )

        st.latex(
            r"Conversion = \frac{Conversions}{Clicks} \times 100"
        )

    with st.expander("CPA"):

        st.write(
            "Le CPA représente le coût moyen nécessaire "
            "pour obtenir une conversion."
        )

        st.latex(
            r"CPA = \frac{Budget}{Conversions}"
        )

    with st.expander("ROI"):

        st.write(
            "Le ROI mesure la rentabilité estimée "
            "d'une campagne marketing."
        )

        st.latex(
            r"ROI = \frac{Gain - Investissement}{Investissement} \times 100"
        )

    st.divider()

    st.subheader("Disponibilité des analyses")

    if segmented is not None:

        st.success(
            "Segmentation disponible"
        )

    else:

        st.warning(
            "Segmentation indisponible"
        )

    if personas is not None:

        st.success(
            "Personas disponibles"
        )

    else:

        st.warning(
            "Personas indisponibles"
        )


# =============================================================================
# HEADER
# =============================================================================

st.title(
    "Dashboard Marketing IA"
)

st.markdown(
    """
    <div class="section-description">

    <b>Segmentation client</b> ·
    <b>Performance marketing</b> ·
    <b>Analyse des ventes</b>

    <br>

    Ce tableau de bord permet d'explorer les données clients,
    d'évaluer les performances des campagnes marketing et
    d'identifier les principaux facteurs contribuant au revenu.

    </div>
    """,
    unsafe_allow_html=True
)

st.divider()


# =============================================================================
# CALCUL DES KPI GLOBAUX
# =============================================================================

total_clients = len(customers)

total_revenue = sales["Revenue"].sum()

total_budget = marketing["Budget"].sum()

total_conversions = marketing["Conversions"].sum()

total_clicks = marketing["Clicks"].sum()

total_impressions = marketing["Impressions"].sum()

roi_moyen = marketing["ROI (%)"].mean()

ctr_global = (
    total_clicks / total_impressions * 100
    if total_impressions > 0
    else 0
)

conversion_global = (
    total_conversions / total_clicks * 100
    if total_clicks > 0
    else 0
)

cpa_global = (
    total_budget / total_conversions
    if total_conversions > 0
    else 0
)


# =============================================================================
# KPI PRINCIPAUX
# =============================================================================

st.subheader(
    "Vue d'ensemble"
)

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Clients",
        f"{total_clients:,}",
        help="Nombre total de clients dans la base."
    )

with col2:

    st.metric(
        "Revenu total",
        f"{total_revenue:,.0f} €",
        help="Revenu total généré par les ventes."
    )

with col3:

    st.metric(
        "Budget marketing",
        f"{total_budget:,.0f} €",
        help="Budget total investi dans les campagnes."
    )

with col4:

    st.metric(
        "ROI moyen",
        f"{roi_moyen:.1f} %",
        help="Retour sur investissement moyen estimé."
    )


# =============================================================================
# KPI MARKETING
# =============================================================================

st.subheader(
    "Indicateurs de performance marketing"
)

col5, col6, col7, col8 = st.columns(4)

with col5:

    st.metric(
        "CTR global",
        f"{ctr_global:.2f} %",
        help="Pourcentage d'impressions ayant généré un clic."
    )

with col6:

    st.metric(
        "Taux de conversion",
        f"{conversion_global:.2f} %",
        help="Pourcentage de clics transformés en conversions."
    )

with col7:

    st.metric(
        "CPA",
        f"{cpa_global:,.2f} €",
        help="Coût moyen pour obtenir une conversion."
    )

with col8:

    st.metric(
        "Conversions",
        f"{total_conversions:,}",
        help="Nombre total de conversions."
    )


st.divider()


# =============================================================================
# INTERPRÉTATION DES KPI
# =============================================================================

with st.expander(
    "Interprétation des principaux indicateurs"
):

    st.markdown(
        """
        **CTR — Click Through Rate**

        Le CTR mesure l'attractivité d'une campagne.
        Une valeur élevée indique qu'une proportion importante
        des impressions génère un clic.

        **Taux de conversion**

        Il mesure l'efficacité des campagnes après le clic.
        Une valeur élevée signifie qu'une proportion importante
        des clics aboutit à une conversion.

        **CPA — Cost Per Acquisition**

        Le CPA indique le coût moyen nécessaire pour obtenir
        une conversion. À qualité de conversion comparable,
        une valeur plus faible est généralement préférable.

        **ROI — Return On Investment**

        Le ROI permet d'évaluer la rentabilité estimée
        d'un investissement marketing.

        - ROI supérieur à 0 % : gain estimé supérieur à l'investissement
        - ROI égal à 0 % : équilibre
        - ROI inférieur à 0 % : perte estimée

        Le ROI présenté ici constitue une estimation basée
        sur le revenu moyen des ventes.
        """
    )


# =============================================================================
# ONGLETS
# =============================================================================

tab1, tab2, tab3 = st.tabs(
    [
        "Segmentation clients",
        "Performance campagnes",
        "Ventes et produits"
    ]
)


# =============================================================================
# TAB 1 — SEGMENTATION
# =============================================================================

with tab1:

    st.header(
        "Segmentation des clients"
    )

    st.markdown(
        """
        <div class="section-description">

        La segmentation consiste à regrouper les clients présentant
        des caractéristiques ou comportements similaires.

        Elle permet d'identifier des profils homogènes et d'adapter
        les stratégies marketing aux différents segments.

        </div>
        """,
        unsafe_allow_html=True
    )

    if segmented is not None:

        # ---------------------------------------------------------------------
        # FILTRE CLUSTER
        # ---------------------------------------------------------------------

        clusters = sorted(
            segmented["Cluster_KMeans"]
            .dropna()
            .unique()
        )

        cluster_filter = st.multiselect(
            "Filtrer les clusters",
            options=clusters,
            default=clusters
        )

        filtered = segmented[
            segmented["Cluster_KMeans"].isin(
                cluster_filter
            )
        ]

        # ---------------------------------------------------------------------
        # KPI SEGMENTATION
        # ---------------------------------------------------------------------

        c1, c2, c3 = st.columns(3)

        with c1:

            st.metric(
                "Clients sélectionnés",
                f"{len(filtered):,}"
            )

        with c2:

            if "Total_Spent" in filtered.columns:

                st.metric(
                    "Dépense moyenne",
                    f"{filtered['Total_Spent'].mean():,.0f} €"
                )

        with c3:

            if "Nb_Achats" in filtered.columns:

                st.metric(
                    "Nombre moyen d'achats",
                    f"{filtered['Nb_Achats'].mean():.1f}"
                )

        st.divider()

        # ---------------------------------------------------------------------
        # TABLEAU CLIENTS
        # ---------------------------------------------------------------------

        st.subheader(
            "Détail des clients"
        )

        columns_client = [
            "Customer_ID",
            "Name",
            "Age",
            "Total_Spent",
            "Nb_Achats",
            "Revenu_Total",
            "Cluster_KMeans"
        ]

        columns_client = [
            column
            for column in columns_client
            if column in filtered.columns
        ]

        st.dataframe(
            filtered[columns_client],
            width="stretch",
            hide_index=True
        )

        # ---------------------------------------------------------------------
        # PERSONAS
        # ---------------------------------------------------------------------

        if personas is not None:

            st.subheader(
                "Personas clients"
            )

            st.markdown(
                """
                Les personas fournissent une interprétation marketing
                des différents groupes obtenus après segmentation.
                """
            )

            for _, persona in personas.iterrows():

                nom = persona.get(
                    "Nom_persona",
                    "Persona"
                )

                clients_persona = persona.get(
                    "Clients",
                    "N/A"
                )

                description = persona.get(
                    "Description",
                    ""
                )

                with st.expander(
                    str(nom)
                ):

                    st.write(
                        f"**Clients :** {clients_persona}"
                    )

                    st.write(
                        description
                    )

        # ---------------------------------------------------------------------
        # FIGURE — SEGMENTATION
        # ---------------------------------------------------------------------

        if (
            "Age" in filtered.columns
            and "Total_Spent" in filtered.columns
            and "Cluster_KMeans" in filtered.columns
        ):

            st.subheader(
                "Analyse graphique de la segmentation"
            )

            fig, ax = plt.subplots(
                figsize=(11, 6)
            )

            unique_clusters = sorted(
                filtered["Cluster_KMeans"].unique()
            )

            for cluster in unique_clusters:

                cluster_data = filtered[
                    filtered["Cluster_KMeans"] == cluster
                ]

                ax.scatter(
                    cluster_data["Age"],
                    cluster_data["Total_Spent"],
                    s=80,
                    alpha=0.75,
                    label=f"Cluster {cluster}"
                )

            # -----------------------------------------------------------------
            # ANNOTATIONS CLIENTS
            # -----------------------------------------------------------------

            if "Name" in filtered.columns:

                for _, row in filtered.iterrows():

                    ax.annotate(
                        str(row["Name"]),
                        (
                            row["Age"],
                            row["Total_Spent"]
                        ),
                        textcoords="offset points",
                        xytext=(4, 4),
                        fontsize=7
                    )

            ax.set_xlabel(
                "Âge du client"
            )

            ax.set_ylabel(
                "Dépenses totales (€)"
            )

            ax.set_title(
                "Segmentation des clients selon l'âge et les dépenses",
                fontsize=13,
                fontweight="bold"
            )

            ax.legend(
                title="Segment",
                loc="best"
            )

            ax.grid(
                alpha=0.25
            )

            fig.tight_layout()

            st.pyplot(
                fig,
                width="stretch"
            )

            plt.close(fig)

            st.markdown(
                """
                <div class="figure-caption">

                <div class="figure-title">
                Figure 1 — Segmentation des clients selon l'âge et les dépenses
                </div>

                <b>Légende :</b>
                Chaque point représente un client.
                L'axe horizontal indique l'âge du client et l'axe vertical
                représente ses dépenses totales. La légende identifie le
                cluster auquel appartient chaque client selon la segmentation
                K-Means.

                <br><br>

                <b>Interprétation :</b>
                Les clients présentant des positions proches dans l'espace
                représenté possèdent des caractéristiques similaires selon
                les variables utilisées pour la segmentation.

                </div>
                """,
                unsafe_allow_html=True
            )

        # ---------------------------------------------------------------------
        # PROFIL DES CLUSTERS
        # ---------------------------------------------------------------------

        if (
            "Cluster_KMeans" in filtered.columns
            and "Total_Spent" in filtered.columns
        ):

            st.subheader(
                "Profil moyen des clusters"
            )

            cluster_profile = (
                filtered
                .groupby("Cluster_KMeans")
                .agg(
                    Clients=("Cluster_KMeans", "size"),
                    Depense_Moyenne=("Total_Spent", "mean")
                )
                .round(2)
            )

            st.dataframe(
                cluster_profile,
                width="stretch"
            )

            st.caption(
                "Le tableau présente le nombre de clients et la dépense "
                "moyenne pour chaque cluster."
            )

    else:

        st.warning(
            "Les données de segmentation ne sont pas disponibles."
        )

        st.info(
            "Exécutez d'abord les modules de segmentation "
            "afin de générer customers_segmented.csv."
        )


# =============================================================================
# TAB 2 — PERFORMANCE CAMPAGNES
# =============================================================================

with tab2:

    st.header(
        "Performance des campagnes"
    )

    st.markdown(
        """
        <div class="section-description">

        Cette section permet de comparer les différents canaux marketing
        selon leur visibilité, leur engagement, leur capacité de conversion,
        leur coût d'acquisition et leur rentabilité estimée.

        </div>
        """,
        unsafe_allow_html=True
    )

    # -------------------------------------------------------------------------
    # FILTRE CANAL
    # -------------------------------------------------------------------------

    channels = sorted(
        marketing["Channel"]
        .dropna()
        .unique()
    )

    channel_filter = st.multiselect(
        "Filtrer par canal",
        options=channels,
        default=channels
    )

    filtered_mkt = marketing[
        marketing["Channel"].isin(
            channel_filter
        )
    ]

    # -------------------------------------------------------------------------
    # KPI
    # -------------------------------------------------------------------------

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(
            "Campagnes",
            f"{len(filtered_mkt):,}"
        )

    with c2:

        st.metric(
            "Budget",
            f"{filtered_mkt['Budget'].sum():,.0f} €"
        )

    with c3:

        st.metric(
            "Conversions",
            f"{filtered_mkt['Conversions'].sum():,.0f}"
        )

    with c4:

        roi_filtre = (
            filtered_mkt["ROI (%)"].mean()
            if len(filtered_mkt) > 0
            else 0
        )

        st.metric(
            "ROI moyen",
            f"{roi_filtre:.1f} %"
        )

    st.divider()

    # -------------------------------------------------------------------------
    # TABLEAU
    # -------------------------------------------------------------------------

    st.subheader(
        "Détail des campagnes"
    )

    columns_marketing = [
        "Campaign_ID",
        "Channel",
        "Budget",
        "Impressions",
        "Clicks",
        "Conversions",
        "CTR (%)",
        "Taux_Conversion (%)",
        "CPA (€)",
        "ROI (%)"
    ]

    columns_marketing = [
        column
        for column in columns_marketing
        if column in filtered_mkt.columns
    ]

    st.dataframe(
        filtered_mkt[columns_marketing],
        width="stretch",
        hide_index=True
    )

    st.divider()

    # -------------------------------------------------------------------------
    # CALCUL DES INDICATEURS PAR CANAL
    # -------------------------------------------------------------------------

    roi_channel = (
        filtered_mkt
        .groupby("Channel")["ROI (%)"]
        .mean()
        .sort_values(
            ascending=False
        )
    )

    cpa_channel = (
        filtered_mkt
        .groupby("Channel")["CPA (€)"]
        .mean()
        .sort_values(
            ascending=True
        )
    )

    channel_performance = (
        filtered_mkt
        .groupby("Channel")[
            [
                "CTR (%)",
                "Taux_Conversion (%)"
            ]
        ]
        .mean()
        .round(2)
    )

    # -------------------------------------------------------------------------
    # FIGURE 2 — ROI
    # -------------------------------------------------------------------------

    if len(roi_channel) > 0:

        st.subheader(
            "ROI moyen par canal"
        )

        fig, ax = plt.subplots(
            figsize=(10, 5.5)
        )

        roi_channel.plot(
            kind="bar",
            ax=ax
        )

        ax.set_xlabel(
            "Canal marketing"
        )

        ax.set_ylabel(
            "ROI moyen (%)"
        )

        ax.set_title(
            "Performance moyenne des canaux selon le ROI",
            fontsize=13,
            fontweight="bold"
        )

        ax.tick_params(
            axis="x",
            rotation=0
        )

        ax.grid(
            axis="y",
            alpha=0.25
        )

        fig.tight_layout()

        st.pyplot(
            fig,
            width="stretch"
        )

        plt.close(fig)

        st.markdown(
            """
            <div class="figure-caption">

            <div class="figure-title">
            Figure 2 — ROI moyen par canal marketing
            </div>

            <b>Légende :</b>
            Chaque barre représente le ROI moyen estimé pour un canal
            marketing. Une valeur élevée indique une rentabilité estimée
            plus importante selon la méthode de calcul utilisée.

            </div>
            """,
            unsafe_allow_html=True
        )

    # -------------------------------------------------------------------------
    # FIGURE 3 — CPA
    # -------------------------------------------------------------------------

    if len(cpa_channel) > 0:

        st.subheader(
            "CPA moyen par canal"
        )

        fig, ax = plt.subplots(
            figsize=(10, 5.5)
        )

        cpa_channel.plot(
            kind="bar",
            ax=ax
        )

        ax.set_xlabel(
            "Canal marketing"
        )

        ax.set_ylabel(
            "CPA moyen (€)"
        )

        ax.set_title(
            "Coût moyen d'acquisition par canal",
            fontsize=13,
            fontweight="bold"
        )

        ax.tick_params(
            axis="x",
            rotation=0
        )

        ax.grid(
            axis="y",
            alpha=0.25
        )

        fig.tight_layout()

        st.pyplot(
            fig,
            width="stretch"
        )

        plt.close(fig)

        st.markdown(
            """
            <div class="figure-caption">

            <div class="figure-title">
            Figure 3 — CPA moyen par canal marketing
            </div>

            <b>Légende :</b>
            Le CPA correspond au coût moyen nécessaire pour obtenir
            une conversion. Une valeur plus faible indique un coût
            d'acquisition plus faible, toutes choses égales par ailleurs.

            </div>
            """,
            unsafe_allow_html=True
        )

    # -------------------------------------------------------------------------
    # FIGURE 4 — CTR / CONVERSION
    # -------------------------------------------------------------------------

    if len(channel_performance) > 0:

        st.subheader(
            "Engagement et conversion par canal"
        )

        fig, ax = plt.subplots(
            figsize=(11, 5.5)
        )

        channel_performance.plot(
            kind="bar",
            ax=ax
        )

        ax.set_xlabel(
            "Canal marketing"
        )

        ax.set_ylabel(
            "Taux moyen (%)"
        )

        ax.set_title(
            "Comparaison du CTR et du taux de conversion",
            fontsize=13,
            fontweight="bold"
        )

        ax.legend(
            title="Indicateur"
        )

        ax.tick_params(
            axis="x",
            rotation=0
        )

        ax.grid(
            axis="y",
            alpha=0.25
        )

        fig.tight_layout()

        st.pyplot(
            fig,
            width="stretch"
        )

        plt.close(fig)

        st.markdown(
            """
            <div class="figure-caption">

            <div class="figure-title">
            Figure 4 — Engagement et conversion par canal
            </div>

            <b>Légende :</b>
            Le CTR mesure la proportion d'impressions ayant généré un clic.
            Le taux de conversion mesure la proportion de clics ayant
            abouti à une conversion.

            <br><br>

            <b>Lecture :</b>
            Un canal peut présenter un CTR élevé sans nécessairement
            présenter un taux de conversion élevé. Les deux indicateurs
            doivent donc être analysés conjointement.

            </div>
            """,
            unsafe_allow_html=True
        )

    # -------------------------------------------------------------------------
    # ANALYSE AUTOMATIQUE
    # -------------------------------------------------------------------------

    if len(filtered_mkt) > 0:

        best_roi_channel = roi_channel.idxmax()

        best_roi_value = roi_channel.max()

        best_cpa_channel = cpa_channel.idxmin()

        best_cpa_value = cpa_channel.min()

        st.subheader(
            "Analyse automatique"
        )

        st.markdown(
            f"""
            <div class="success-box">

            <b>Canal présentant le meilleur ROI moyen :</b>
            {best_roi_channel}

            <br>

            ROI moyen estimé :
            <b>{best_roi_value:.1f} %</b>

            <br><br>

            <b>Canal présentant le CPA moyen le plus faible :</b>
            {best_cpa_channel}

            <br>

            CPA moyen :
            <b>{best_cpa_value:.2f} €</b>

            </div>
            """,
            unsafe_allow_html=True
        )


# =============================================================================
# TAB 3 — VENTES & PRODUITS
# =============================================================================

with tab3:

    st.header(
        "Ventes et produits"
    )

    st.markdown(
        """
        <div class="section-description">

        Cette section permet d'analyser les ventes et d'identifier
        les catégories de produits contribuant le plus au revenu total.

        </div>
        """,
        unsafe_allow_html=True
    )

    # -------------------------------------------------------------------------
    # JOINTURE
    # -------------------------------------------------------------------------

    sales_products = sales.merge(
        products,
        on="Product_ID",
        how="left"
    )

    # -------------------------------------------------------------------------
    # KPI
    # -------------------------------------------------------------------------

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "Nombre de ventes",
            f"{len(sales_products):,}"
        )

    with c2:

        st.metric(
            "Revenu total",
            f"{sales_products['Revenue'].sum():,.0f} €"
        )

    with c3:

        if "Quantity" in sales_products.columns:

            st.metric(
                "Quantité vendue",
                f"{sales_products['Quantity'].sum():,.0f}"
            )

    st.divider()

    # -------------------------------------------------------------------------
    # TABLEAU
    # -------------------------------------------------------------------------

    st.subheader(
        "Détail des ventes"
    )

    st.dataframe(
        sales_products,
        width="stretch",
        hide_index=True
    )

    # -------------------------------------------------------------------------
    # REVENU PAR CATEGORIE
    # -------------------------------------------------------------------------

    if "Category" in sales_products.columns:

        st.subheader(
            "Revenu par catégorie"
        )

        rev_categorie = (
            sales_products
            .groupby("Category")["Revenue"]
            .sum()
            .sort_values(
                ascending=False
            )
        )

        fig, ax = plt.subplots(
            figsize=(10, 5.5)
        )

        rev_categorie.plot(
            kind="bar",
            ax=ax
        )

        ax.set_xlabel(
            "Catégorie de produit"
        )

        ax.set_ylabel(
            "Revenu total (€)"
        )

        ax.set_title(
            "Contribution des catégories au revenu total",
            fontsize=13,
            fontweight="bold"
        )

        ax.tick_params(
            axis="x",
            rotation=0
        )

        ax.grid(
            axis="y",
            alpha=0.25
        )

        fig.tight_layout()

        st.pyplot(
            fig,
            width="stretch"
        )

        plt.close(fig)

        st.markdown(
            """
            <div class="figure-caption">

            <div class="figure-title">
            Figure 5 — Revenu total par catégorie de produit
            </div>

            <b>Légende :</b>
            Chaque barre représente le revenu total généré par une
            catégorie de produits. Les catégories sont classées par
            contribution décroissante au revenu.

            </div>
            """,
            unsafe_allow_html=True
        )

        # ---------------------------------------------------------------------
        # MEILLEURE CATEGORIE
        # ---------------------------------------------------------------------

        if len(rev_categorie) > 0:

            best_category = (
                rev_categorie.idxmax()
            )

            best_category_revenue = (
                rev_categorie.max()
            )

            st.markdown(
                f"""
                <div class="success-box">

                <b>Catégorie présentant le revenu le plus élevé :</b>
                {best_category}

                <br>

                Revenu généré :
                <b>{best_category_revenue:,.0f} €</b>

                </div>
                """,
                unsafe_allow_html=True
            )


# =============================================================================
# SYNTHÈSE FINALE
# =============================================================================

st.divider()

st.header(
    "Synthèse décisionnelle"
)

st.markdown(
    """
    <div class="section-description">

    L'analyse combinée des données clients, marketing et commerciales
    permet d'obtenir une vision globale de la performance de l'activité.

    </div>
    """,
    unsafe_allow_html=True
)

summary_col1, summary_col2 = st.columns(2)

with summary_col1:

    st.markdown(
        """
        ### Segmentation client

        La segmentation permet d'identifier des groupes de clients
        présentant des caractéristiques similaires. Elle constitue
        une base pour personnaliser les actions marketing et mieux
        cibler les différents profils.

        ### Performance marketing

        L'analyse du CTR, du taux de conversion, du CPA et du ROI
        permet de comparer les canaux marketing et d'identifier
        les investissements présentant les performances les plus
        intéressantes.
        """
    )

with summary_col2:

    st.markdown(
        """
        ### Ventes et produits

        L'analyse du revenu par catégorie permet d'identifier les
        produits ou familles de produits contribuant le plus au
        chiffre d'affaires.

        ### Aide à la décision

        Le croisement de la segmentation client, de la performance
        marketing et des résultats commerciaux fournit une base
        quantitative pour optimiser les campagnes, mieux répartir
        les budgets et prioriser les segments les plus intéressants.
        """
    )


# =============================================================================
# FOOTER
# =============================================================================

st.divider()

st.markdown(
    """
    <div class="footer">

    Module 8 — Dashboard Marketing IA<br>
    Analyse et optimisation marketing basée sur la segmentation client

    </div>
    """,
    unsafe_allow_html=True
)


# In[ ]:




