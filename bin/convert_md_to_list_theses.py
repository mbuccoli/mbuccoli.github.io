import os
import re
from html.parser import HTMLParser
from datetime import datetime

# Configuration
OUTPUT_DIR = "_theses"
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

class ThesisParser():
    def __init__(self):
        self.theses = []
        self.current_thesis = None
    def feed(self, html_block):
        articles = html_block.split(r"<article>")
        for article in articles:
            self.add_thesis(article)
    def add_thesis(self, article_block):
        lines = article_block.split("\n")
        current_thesis = {"title": "", "author": "", "abstract": "", "url": "", "month":"", "year": ""}
        author_next = False
        abstract_next = False
        title_next=False
        for line in lines:
            for tag in [r"<br>",r"</br>",r"<br />",r"<br/>",r"</p>",r"</article>",r"</p>"]:
                line=line.replace(tag, "")
            
            if line=="" or r"<br/>"in line or r"</article>" in line:
                continue
            elif r"<em>" in line or title_next:
                if not title_next:
                    current_thesis["title"] = line.split(r"<em>")[1].split("</em>")[0]
                else:
                    current_thesis["title"] += line.split(r"</em>")[0]
                if r"</em>" not in line:
                    title_next = True
                else:
                    title_next = False
                    author_next=True
            elif author_next:
                # print(line)
                current_thesis["author"] = line.split(",")[0]
                current_thesis["month"] = line.split(", ")[1].split(" ")[0]
                current_thesis["year"] = line.split(", ")[1].split(" ")[1]
                author_next=False
            elif "short abstract" in line.lower():
                abstract_next=True
            elif "read the" in line.lower():
                if "href" in line:
                    current_thesis["url"] = line.split('href="')[1].split('"')[0]            
                
            elif abstract_next:
                current_thesis["abstract"]+= line+" "
        if current_thesis["title"]!="":
            self.theses.append(current_thesis)
 


def save_to_markdown(thesis):
    
    year= thesis['year']
    print(thesis)
    date_obj = datetime.strptime(f"{thesis['month']} {year}", "%B %Y")
    date_fmt = date_obj.strftime("%Y-%m-%d")
    # Filename: surname_year.md
    surname = thesis["author"].split(" ")[-1].lower()
    filename = f"{surname}_{thesis['year']}.md"
    
    content = f"""---
title: {thesis['title']}
date: {date_fmt}
author: {thesis['author']}
layout: thesis
url: {thesis['url']}
---

{thesis['abstract']}
"""
    
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

# Input HTML Data
html_block = """
<article>

<p>

<em>Methods for providing input gain robustness to dnn-based real-time speech processing systems</em><br>

Yilmaz Ugur Ozcan, July 2024 <br>

<strong>Short abstract</strong> 

Input gain variations can significantly impact the performance of DNN-based real-time speech processing systems. 

This thesis explores three methods to enhance robustness against these variations: Gain-Augmented Training, Differential Features, and Smoothed Frame Normalization. 

Experimental results show that these approaches improve the consistency and reliability of DNN outputs under varying input gain condition.

<br/>

<a href="https://www.politesi.polimi.it/handle/10589/223344">Read the full abstract</a><br/>

</p>

</article>



<article>

<p>

<em>A Lightweight Speaker Verification System for Real-Time Applications</em><br>

Eray Ozgunay, July 2024<br>

<strong>Short abstract</strong> 

This work tackles key challenges in Speaker Verification (SV) by introducing a novel, lightweight SV system designed for real-time applications in noisy and reverberant environments. 

The system leverages advanced convolutional techniques within a Deep Neural Network (DNN) and real-time pooling layers to enhance responsiveness and stability across various acoustic conditions. 

While it may not achieve the highest performance levels, it excels in real-time processing, making it ideal for dynamic environments where speed and computational efficiency are crucial.

<br/>

</p>

</article>



<article>

<p>

<em>A cascade approach for speech enhancement based on deep learning</em><br>

Filippo Gualtieri, April 2023<br>

<strong>Short abstract</strong>

We propose a cascaded network with a lightweight phase-unaware approach and an optional more

computationally

demanding phase-aware stage to perform single-channel Speech Enahncement based on Deep Learning

(DL). Our solution performs as good as more complex baselines

in terms of parameters and Floating Point Operations (FLOPs) according to both objective quality

metrics and subjective evaluations

<br />

<!--<a href="<LINK TESI>">Read the full abstract</a><br/>-->

</p>

</article>

<article>

<p>

<em>Real-time multimicrophone speaker separation for the automotive scenario, using a

lightweight convolutional neural network</em><br>

Federico Maver, December 2022<br>

<strong>Short abstract</strong>

We address the multichannel speaker separation problem, and we propose two causal and

lightweight Deep Neural Network (DNN) models that can

adapt to a wide range of microphone positions and distances. The problem focuses on the

automotive scenario.

<br />

<!--<a href="<LINK TESI>">Read the full abstract</a><br/>-->

</p>

</article>





<article>

<p>

<em>Real-time speech dereverberation using asmall-footprint convolutional neural

network</em><br>

Federico Di Marzo, April 2022<br>

<strong>Short abstract</strong>

We propose an innovative technique based on the use of a Convolutional Neural Network (CNN),

designed to offer a small-footprint and optimized computational performance, for systems that

workin real-time,

with minimal latency.

<br />

<!--<a href="<LINK TESI>">Read the full abstract</a><br/>-->

</p>

</article>

<article>

<p>

<em>Speaker recognition with small-footprint CNN</em><br>

Francesco Salani, December 2021<br>

<strong>Short abstract</strong>

A speaker recognition system is a technology that aims to recognize

a person's identity based on their voice.

In this thesis, we propose a low-latency speaker recognition system based on

Deep Neural Networks.

<br />

<!--<a href="<LINK TESI>">Read the full abstract</a><br/>-->

</p>

</article>





<article>

<p>

<em>A deep real-time talk state detector for acoustic echo cancellation</em><br>

Daniele Foscarin, September 2021<br>

<strong>Short abstract</strong>

A novel approach, using a talk state detector (TSD) to enhance the performance of a linear

acoustic echo cancellation.

It consists of a fully convolutional neural network classifier that performs causal processing

to meet the real-time requiremment with less than 8,000 trainable parameters.

<br />

<!--<a href="<LINK TESI>">Read the full abstract</a><br/>-->

</p>

</article>





<article>

<p>

<em>A real-time solution for speech enhancement using dilated convolutional neural

networks</em><br>

Fabio Segato, July 2021<br>

<strong>Short abstract </strong>

In this work, we propose a speech enhancement solution based on Deep Neural Networks that

withstands the strict

requirements imposed by embedded devices in terms of memory footprint and processing power.

The proposed approach operates in real-time, extracting perceptually-relevant features in

an efficient fashion.

<br />

<a href="https://www.politesi.polimi.it/handle/10589/178087">Read the full abstract</a><br />

</p>

</article>





<article>

<p>

<em>A hybrid approach for computationally-efficient beamforming using sparse linear microphone

arrays</em><br>

Davide Balsarri, December 2020<br>

<strong>Short abstract</strong> We propose a hybrid beamforming solution that combines

two methods: one that is efficient for signals with high input SNR and one with low input SNR.

Results show that our SCM-based hybrid

solution outperforms most SCM-based methods and exhibits a lower computational complexity.

<br />

<a href="https://www.politesi.polimi.it/handle/10589/171239">Read the full abstract</a><br />

</p>

</article>



<article>

<p>

<em>Voice activity detection using small-footprint deep learning</em><br>

Luca Menescardi, December 2019<br>

<strong>Short abstract</strong> Techniques employed to detect the presence or absence of human

voice in an audio signal are called Voice Activity Detection

(VAD) algorithms. Our approach optimizes both the feature extraction and the classification

performed by the deep neural network. The goal is to comply with requirements imposed by

embedded systems.

<br />

<a href="https://www.politesi.polimi.it/handle/10589/152919">Read the full abstract</a><br />

</p>

</article>





<article>

<p>

<em>Automatic playlist generation using recurrent neural network</em><br>

Rosilde Tatiana Irene, July 2018<br>

<strong>Short abstract</strong> In this study we propose an automatic playlist generation

approach which analyzes hand-crafted playlists, understands their

structure and generates new playlists accordingly. We have adopted a deep learning architecture,

in particular a Recurrent Neural

Network, which is specialized in sequence modeling. <br />

<a href="https://www.politesi.polimi.it/handle/10589/142101">Read the thesis</a><br />

</p>

</article>







<article>

<p>

<em>Beat tracking using recurrent neural network : a transfer learning approach</em><br>

Davide Fiocchi, April 2018<br>

<strong>Short abstract</strong> In this work, we propose an approach to apply transfer learning

for beat tracking.

We use a deep RNN as the starting network trained on popular music, and we transfer it to track

beats of folk music.

Moreover, we test if the resultant models are able to deal with highly variable music, such as

Greek folk music.<br />

<a href="https://www.politesi.polimi.it/handle/10589/139073">Read the thesis</a><br />

</p>

</article>



<article>

<p>

<em>Learning a personalized similarity metric for musical content</em><br>

Luca Carloni, April 2018<br>

<strong>Short abstract</strong> We present a hybrid model for personalized

similarity modeling that relies on both content-based and user-related similarity information.

We exploit a non-metric scaling technique to first elaborate a

low-dimensional space (or embedding) which fulfills the similarity information provided by the

user, and a regression technique to learn a mapping between

content-based information and embedding-related information. <br />

<a href="https://www.politesi.polimi.it/handle/10589/139076">Read the thesis</a><br />

</p>

</article>



<article>

<p>

<em>A personalized metric for music similarity using Siamese deep neural networks</em><br>

Federico Sala, April 2018<br>

<strong>Short abstract</strong> In this thesis we propose

an approach to model a personalized music similarity metric based on a Deep Neural Network.

We use a first stage for learning a generic music similarity metric relying on a great amount of

data,

and a second stage for customizing it using personalized annotations collected through a survey.

<br />

<a href="https://www.politesi.polimi.it/handle/10589/139078">Read the thesis</a><br />

</p>

</article>



<article>

<p>

<em>Analysis of musical structure : an approach based on deep learning</em><br>

Davide Andreoletti, July 2015<br>

<strong>Short abstract</strong> We propose a Music Structural

Analysis algorithm where we use a Deep Belief Network to extract a sequence of descriptors that

is successively

given as input to several Music Structural Analysis algorithms presented in literature. <br />

<a href="https://www.politesi.polimi.it/handle/10589/108756">Read the thesis</a><br />

</p>

</article>



<article>

<p>

<em>A music search engine based on a contextual related semantic model</em><br>

Alessandro Gallo, April 2014<br>

<strong>Short abstract</strong> In this work we propose an approach for music high-level

description and music retrieval, that we named Contextual-related semantic model. Our method

defines different semantic contexts and dimensional semantic relations between music descriptors

belonging to the same context. <br />

<a href="https://www.politesi.polimi.it/handle/10589/89922">Read the thesis</a><br />

</p>

</article>"""

if __name__ == "__main__":
    parser = ThesisParser()
    parser.feed(html_block)
    
    for t in parser.theses:
        save_to_markdown(t)
    
    print(f"Processed {len(parser.theses)} files into {OUTPUT_DIR}/")