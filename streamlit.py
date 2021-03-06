{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/21a3084/streamlitv2/blob/main/streamlit.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "RCtWeB_E7jt5"
      },
      "outputs": [],
      "source": [
        "!pip install streamlit"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 30,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sOWUzWFj8AI-",
        "outputId": "83c85d3f-4db9-4c58-b922-9bb161a773f8"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Overwriting app.py\n"
          ]
        }
      ],
      "source": [
        "%%writefile app.py\n",
        "import streamlit as st\n",
        "import numpy as np\n",
        "import pandas as pd\n",
        "from PIL import Image\n",
        "import time\n",
        "\n",
        "st.title(\"watashi !\")\n",
        "\n",
        "st.write('プレグレスバーの表示')\n",
        "'Start!!'\n",
        "\n",
        "latest_iteration = st.empty()\n",
        "bar = st.progress(0)\n",
        "\n",
        "for i in range(100):\n",
        "  latest_iteration.text(f'Iteration{i+1}')\n",
        "  bar.progress(i+1)\n",
        "  time.sleep(0.1)\n",
        "\n",
        "'Done!!!!!!!'\n",
        "left_column,right_column =st.columns(2)\n",
        "button=left_column.button('右カラムに文字を表示')\n",
        "if button:\n",
        "    right_column.write('moji')\n",
        "expander1 = st.expander('問い合わせ1')\n",
        "expander1.write('問い合わせ1の内容を書く')\n",
        "expander2 = st.expander('問い合わせ2')\n",
        "expander2.write('問い合わせ2の内容を書く')\n",
        "expander3 = st.expander('問い合わせ3')\n",
        "expander3.write('問い合わせ3の内容を書く')\n",
        "#condition=st.slider('abaaabaabbbaa',0,100,50)\n",
        "#'abababa:',text\n",
        "#'abaaaba',condition\n",
        "#if st.checkbox('Show Image'):\n",
        "#  img = Image.open('efg.jpg')\n",
        "#  st.image(img,caption='watashi',use_column_width=True)\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 27,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2mLaFy9v8QEs",
        "outputId": "3f738965-16b3-489c-8072-ad554c8fa50e"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2022-05-24 02:41:43.805 INFO    numexpr.utils: NumExpr defaulting to 2 threads.\n",
            "\u001b[0m\n",
            "\u001b[34m\u001b[1m  You can now view your Streamlit app in your browser.\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m  Network URL: \u001b[0m\u001b[1mhttp://172.28.0.2:8501\u001b[0m\n",
            "\u001b[34m  External URL: \u001b[0m\u001b[1mhttp://34.132.21.87:8501\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[K\u001b[?25hnpx: installed 22 in 2.392s\n",
            "your url is: https://brave-rules-suffer-34-132-21-87.loca.lt\n",
            "\u001b[34m  Stopping...\u001b[0m\n",
            "^C\n"
          ]
        }
      ],
      "source": [
        "!streamlit run app.py & sleep 3 && npx localtunnel --port 8501"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "name": "streamlit.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyPzBWX8GpPla5uswo3C3K5/",
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
