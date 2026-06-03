{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMEsIAoUIr9aFUvQndUOkNb"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/octarine-labs/dash/blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "3hnEPEWwff6-",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "afce8287-23dc-4ced-f1e1-03849dc4e23a"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing app.py\n"
          ]
        }
      ],
      "source": [
        "%%writefile app.py\n",
        "import streamlit as st\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "import plotly.express as px\n",
        "\n",
        "st.title(\"📊 Dasbor Visualisasi Data Gratis\")\n",
        "st.write(\"Aplikasi ini dibuat gratis tanpa resource komputer lokal!\")\n",
        "\n",
        "# Membuat data tiruan\n",
        "chart_data = pd.DataFrame(\n",
        "    np.random.randn(20, 3),\n",
        "    columns=['Pendapatan', 'Pengeluaran', 'Keuntungan']\n",
        ")\n",
        "\n",
        "# Membuat grafik interaktif dengan Plotly\n",
        "fig = px.line(chart_data, title=\"Tren Keuangan Perusahaan\")\n",
        "st.plotly_chart(fig)\n"
      ]
    }
  ]
}
