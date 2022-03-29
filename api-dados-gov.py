{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled0.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMpYKX0t6x0aIIkJo+1GsXF",
      "include_colab_link": true
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
        "<a href=\"https://colab.research.google.com/github/eduardollopes/data-ingestion/blob/main/api-dados-gov.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "qBf57belaoUc"
      },
      "outputs": [],
      "source": [
        "import pandas as pd \n",
        "import requests\n",
        "from bs4 import BeautifulSoup\n",
        "from io import StringIO"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "git"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 166
        },
        "id": "ox4MF4zAN1ni",
        "outputId": "4e356858-f387-4dfd-bf63-4634f174ad15"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "error",
          "ename": "NameError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-12-b40508769cb0>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mgit\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m: name 'git' is not defined"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "metadata": {
        "id": "UCRxf3hCOGNf"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "url = 'http://repositorio.dados.gov.br/seges/comprasnet_contratos/anual/'\n",
        "param = ['2021' , '2022']\n",
        "\n",
        "list_url = []\n",
        "for year in param:\n",
        "  mycontent = requests.get(url+year)\n",
        "  html = mycontent.text\n",
        "  soup = BeautifulSoup(mycontent.content, \"html.parser\")\n",
        "  for link in soup.find_all('a'):\n",
        "    if '.csv' in str(link):\n",
        "      csv_url = url + year + '/' + link.get('href')\n",
        "      list_url.append(csv_url)"
      ],
      "metadata": {
        "id": "O4kHyimByvQ3"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "display(list_url)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 445
        },
        "id": "6Vy5hADYtdnu",
        "outputId": "c376297d-9e58-44e2-8deb-fc2f69f8a19c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "['http://repositorio.dados.gov.br/seges/comprasnet_contratos/anual/2021/comprasnet-contratos-anual-arquivos-2021.csv',\n",
              " 'http://repositorio.dados.gov.br/seges/comprasnet_contratos/anual/2021/comprasnet-contratos-anual-contratos-2021.csv',\n",
              " 'http://repositorio.dados.gov.br/seges/comprasnet_contratos/anual/2021/comprasnet-contratos-anual-cronogramas-2021.csv',\n",
              " 'http://repositorio.dados.gov.br/seges/comprasnet_contratos/anual/2021/comprasnet-contratos-anual-despesas_acessorias-2021.csv',\n",
              " 'http://repositorio.dados.gov.br/seges/comprasnet_contratos/anual/2021/comprasnet-contratos-anual-empenhos-2021.csv',\n",
              " 'http://repositorio.dados.gov.br/seges/comprasnet_contratos/anual/2021/comprasnet-contratos-anual-faturas-2021.csv',\n",
              " 'http://repositorio.dados.gov.br/seges/comprasnet_contratos/anual/2021/comprasnet-contratos-anual-garantias-2021.csv',\n",
              " 'http://repositorio.dados.gov.br/seges/comprasnet_contratos/anual/2021/comprasnet-contratos-anual-historicos-2021.csv',\n",
              " 'http://repositorio.dados.gov.br/seges/comprasnet_contratos/anual/2021/comprasnet-contratos-anual-itens-2021.csv',\n",
              " 'http://repositorio.dados.gov.br/seges/comprasnet_contratos/anual/2021/comprasnet-contratos-anual-prepostos-2021.csv',\n",
              " 'http://repositorio.dados.gov.br/seges/comprasnet_contratos/anual/2021/comprasnet-contratos-anual-responsaveis-2021.csv',\n",
              " 'http://repositorio.dados.gov.br/seges/comprasnet_contratos/anual/2021/comprasnet-contratos-anual-terceirizados-2021.csv',\n",
              " 'http://repositorio.dados.gov.br/seges/comprasnet_contratos/anual/2022/comprasnet-contratos-anual-arquivos-2022.csv',\n",
              " 'http://repositorio.dados.gov.br/seges/comprasnet_contratos/anual/2022/comprasnet-contratos-anual-contratos-2022.csv',\n",
              " 'http://repositorio.dados.gov.br/seges/comprasnet_contratos/anual/2022/comprasnet-contratos-anual-cronogramas-2022.csv',\n",
              " 'http://repositorio.dados.gov.br/seges/comprasnet_contratos/anual/2022/comprasnet-contratos-anual-despesas_acessorias-2022.csv',\n",
              " 'http://repositorio.dados.gov.br/seges/comprasnet_contratos/anual/2022/comprasnet-contratos-anual-empenhos-2022.csv',\n",
              " 'http://repositorio.dados.gov.br/seges/comprasnet_contratos/anual/2022/comprasnet-contratos-anual-faturas-2022.csv',\n",
              " 'http://repositorio.dados.gov.br/seges/comprasnet_contratos/anual/2022/comprasnet-contratos-anual-garantias-2022.csv',\n",
              " 'http://repositorio.dados.gov.br/seges/comprasnet_contratos/anual/2022/comprasnet-contratos-anual-historicos-2022.csv',\n",
              " 'http://repositorio.dados.gov.br/seges/comprasnet_contratos/anual/2022/comprasnet-contratos-anual-itens-2022.csv',\n",
              " 'http://repositorio.dados.gov.br/seges/comprasnet_contratos/anual/2022/comprasnet-contratos-anual-prepostos-2022.csv',\n",
              " 'http://repositorio.dados.gov.br/seges/comprasnet_contratos/anual/2022/comprasnet-contratos-anual-responsaveis-2022.csv',\n",
              " 'http://repositorio.dados.gov.br/seges/comprasnet_contratos/anual/2022/comprasnet-contratos-anual-terceirizados-2022.csv']"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for df_row in list_url:\n",
        "  url = df_row\n",
        "  s = requests.get(url).content\n",
        "  df = pd.read_csv(StringIO(s.decode('utf-8')) , low_memory=False)\n",
        "  # print('Arquivo: ' , df_row.split('/')[7] , ' | Qtd Linhas: ' , df.shape[0])\n",
        "  print(list(df.columns))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FVwbNYp60hcG",
        "outputId": "5a556d72-3837-4111-9b0c-b152d9e44fb4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['id', 'contrato_id', 'tipo', 'processo', 'sequencial_documento', 'descricao', 'arquivos']\n",
            "['id', 'receita_despesa', 'numero', 'orgao_codigo', 'orgao_nome', 'unidade_codigo', 'unidade_nome_resumido', 'unidade_nome', 'fornecedor_tipo', 'fonecedor_cnpj_cpf_idgener', 'fornecedor_nome', 'codigo_tipo', 'tipo', 'categoria', 'processo', 'objeto', 'fundamento_legal', 'informacao_complementar', 'codigo_modalidade', 'modalidade', 'unidade_compra', 'licitacao_numero', 'data_assinatura', 'data_publicacao', 'vigencia_inicio', 'vigencia_fim', 'valor_inicial', 'valor_global', 'num_parcelas', 'valor_parcela', 'valor_acumulado']\n",
            "['id', 'contrato_id', 'tipo', 'numero', 'receita_despesa', 'observacao', 'mesref', 'anoref', 'vencimento', 'retroativo', 'valor']\n",
            "['id', 'contrato_id', 'tipo_id', 'recorrencia_id', 'descricao_complementar', 'vencimento', 'valor']\n",
            "['id', 'contrato_id', 'numero', 'credor', 'fonte_recurso', 'planointerno', 'naturezadespesa', 'empenhado', 'aliquidar', 'liquidado', 'pago', 'rpinscrito', 'rpaliquidar', 'rpliquidado', 'rppago']\n",
            "['id', 'contrato_id', 'tipolistafatura_id', 'justificativafatura_id', 'numero', 'emissao', 'prazo', 'vencimento', 'valor', 'juros', 'multa', 'glosa', 'valorliquido', 'processo', 'protocolo', 'ateste', 'repactuacao', 'infcomplementar', 'mesref', 'anoref', 'situacao']\n",
            "['id', 'contrato_id', 'tipo', 'valor', 'vencimento']\n",
            "['id', 'contrato_id', 'receita_despesa', 'numero', 'observacao', 'ug', 'gestao', 'fornecedor', 'codigo_tipo', 'tipo', 'categoria', 'processo', 'objeto', 'fundamento_legal_aditivo', 'informacao_complementar', 'modalidade', 'licitacao_numero', 'codigo_unidade_origem', 'nome_unidade_origem', 'data_assinatura', 'data_publicacao', 'vigencia_inicio', 'vigencia_fim', 'valor_inicial', 'valor_global', 'num_parcelas', 'valor_parcela', 'novo_valor_global', 'novo_num_parcelas', 'novo_valor_parcela', 'data_inicio_novo_valor', 'retroativo', 'retroativo_mesref_de', 'retroativo_anoref_de', 'retroativo_mesref_ate', 'retroativo_anoref_ate', 'retroativo_vencimento', 'retroativo_valor']\n",
            "['id', 'contrato_id', 'tipo_id', 'grupo_id', 'catmatseritem_id', 'descricao_complementar', 'quantidade', 'valorunitario', 'valortotal']\n",
            "['id', 'contrato_id', 'doc_formalizacao', 'informacao_complementar', 'data_inicio', 'data_fim', 'situacao']\n",
            "['id', 'contrato_id', 'funcao_id', 'instalacao_id', 'portaria', 'situacao', 'data_inicio', 'data_fim']\n",
            "['id', 'contrato_id', 'funcao_id', 'descricao_complementar', 'jornada', 'unidade', 'custo', 'escolaridade_id', 'data_inicio', 'data_fim', 'situacao', 'aux_transporte', 'vale_alimentacao']\n",
            "['id', 'contrato_id', 'tipo', 'processo', 'sequencial_documento', 'descricao', 'arquivos']\n",
            "['id', 'receita_despesa', 'numero', 'orgao_codigo', 'orgao_nome', 'unidade_codigo', 'unidade_nome_resumido', 'unidade_nome', 'fornecedor_tipo', 'fonecedor_cnpj_cpf_idgener', 'fornecedor_nome', 'codigo_tipo', 'tipo', 'categoria', 'processo', 'objeto', 'fundamento_legal', 'informacao_complementar', 'codigo_modalidade', 'modalidade', 'unidade_compra', 'licitacao_numero', 'data_assinatura', 'data_publicacao', 'vigencia_inicio', 'vigencia_fim', 'valor_inicial', 'valor_global', 'num_parcelas', 'valor_parcela', 'valor_acumulado', 'situacao']\n",
            "['id', 'contrato_id', 'tipo', 'numero', 'receita_despesa', 'observacao', 'mesref', 'anoref', 'vencimento', 'retroativo', 'valor']\n",
            "['id', 'contrato_id', 'tipo_id', 'recorrencia_id', 'descricao_complementar', 'vencimento', 'valor']\n",
            "['id', 'contrato_id', 'numero', 'credor', 'fonte_recurso', 'planointerno', 'naturezadespesa', 'empenhado', 'aliquidar', 'liquidado', 'pago', 'rpinscrito', 'rpaliquidar', 'rpliquidado', 'rppago']\n",
            "['id', 'contrato_id', 'tipolistafatura_id', 'justificativafatura_id', 'numero', 'emissao', 'prazo', 'vencimento', 'valor', 'juros', 'multa', 'glosa', 'valorliquido', 'processo', 'protocolo', 'ateste', 'repactuacao', 'infcomplementar', 'mesref', 'anoref', 'situacao']\n",
            "['id', 'contrato_id', 'tipo', 'valor', 'vencimento']\n",
            "['id', 'contrato_id', 'receita_despesa', 'numero', 'observacao', 'ug', 'gestao', 'fornecedor', 'codigo_tipo', 'tipo', 'categoria', 'processo', 'objeto', 'fundamento_legal_aditivo', 'informacao_complementar', 'modalidade', 'licitacao_numero', 'codigo_unidade_origem', 'nome_unidade_origem', 'data_assinatura', 'data_publicacao', 'vigencia_inicio', 'vigencia_fim', 'valor_inicial', 'valor_global', 'num_parcelas', 'valor_parcela', 'novo_valor_global', 'novo_num_parcelas', 'novo_valor_parcela', 'data_inicio_novo_valor', 'retroativo', 'retroativo_mesref_de', 'retroativo_anoref_de', 'retroativo_mesref_ate', 'retroativo_anoref_ate', 'retroativo_vencimento', 'retroativo_valor']\n",
            "['id', 'contrato_id', 'tipo_id', 'grupo_id', 'catmatseritem_id', 'descricao_complementar', 'quantidade', 'valorunitario', 'valortotal']\n",
            "['id', 'contrato_id', 'doc_formalizacao', 'informacao_complementar', 'data_inicio', 'data_fim', 'situacao']\n",
            "['id', 'contrato_id', 'funcao_id', 'instalacao_id', 'portaria', 'situacao', 'data_inicio', 'data_fim']\n",
            "['id', 'contrato_id', 'funcao_id', 'descricao_complementar', 'jornada', 'unidade', 'custo', 'escolaridade_id', 'data_inicio', 'data_fim', 'situacao', 'aux_transporte', 'vale_alimentacao']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df = str()\n",
        "\n",
        "# for df_row in list_url:\n",
        "#   if df is None:\n",
        "#     url = df_row\n",
        "#     s = requests.get(url).content\n",
        "#     df = pd.read_csv(StringIO(s.decode('utf-8')))\n",
        "#   else:\n",
        "#     df = pd.concat([df])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 353
        },
        "id": "cNSDAfwxxhnQ",
        "outputId": "b2b45e4f-9882-4c10-80a2-7e925246d629"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "TypeError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-26-c2d176d9b867>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      7\u001b[0m     \u001b[0mdf\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread_csv\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mStringIO\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ms\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdecode\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'utf-8'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      8\u001b[0m   \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 9\u001b[0;31m     \u001b[0mdf\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mconcat\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mdf\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;32m/usr/local/lib/python3.7/dist-packages/pandas/util/_decorators.py\u001b[0m in \u001b[0;36mwrapper\u001b[0;34m(*args, **kwargs)\u001b[0m\n\u001b[1;32m    309\u001b[0m                     \u001b[0mstacklevel\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mstacklevel\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    310\u001b[0m                 )\n\u001b[0;32m--> 311\u001b[0;31m             \u001b[0;32mreturn\u001b[0m \u001b[0mfunc\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    312\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    313\u001b[0m         \u001b[0;32mreturn\u001b[0m \u001b[0mwrapper\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.7/dist-packages/pandas/core/reshape/concat.py\u001b[0m in \u001b[0;36mconcat\u001b[0;34m(objs, axis, join, ignore_index, keys, levels, names, verify_integrity, sort, copy)\u001b[0m\n\u001b[1;32m    302\u001b[0m         \u001b[0mverify_integrity\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mverify_integrity\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    303\u001b[0m         \u001b[0mcopy\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mcopy\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 304\u001b[0;31m         \u001b[0msort\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0msort\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    305\u001b[0m     )\n\u001b[1;32m    306\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.7/dist-packages/pandas/core/reshape/concat.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, objs, axis, join, keys, levels, names, ignore_index, verify_integrity, copy, sort)\u001b[0m\n\u001b[1;32m    382\u001b[0m                     \u001b[0;34m\"only Series and DataFrame objs are valid\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    383\u001b[0m                 )\n\u001b[0;32m--> 384\u001b[0;31m                 \u001b[0;32mraise\u001b[0m \u001b[0mTypeError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmsg\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    385\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    386\u001b[0m             \u001b[0mndims\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0madd\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mobj\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mndim\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mTypeError\u001b[0m: cannot concatenate object of type '<class 'str'>'; only Series and DataFrame objs are valid"
          ]
        }
      ]
    }
  ]
}