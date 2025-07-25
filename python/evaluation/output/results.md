March 10, 2025 at 10:51:26 AM

## Grok 2
I tested the **Grok API** (grok-2; no grok-3 thru the API yet) with the prompt: "Find a recent PubMed article on Major Depression. Summarize it in a way a 10th grader can understand. List references." Here's what I found:  

- **Results**: It sometimes hallucinated articles, and sometimes found real ones.  It got it right 50% of the time.  References/citations were hit-or-miss—correct at times, wrong or incomplete others. It's not super reliable yet.  
- **Performance**: Average response time was 8.39 seconds.  
- **Usage Stats**: Got token details, e.g., Prompt Tokens: 37, Completion Tokens: 595, Total Tokens: 632, with breakdowns like {'text\_tokens': 37, 'audio\_tokens': 0, 'image\_tokens': 0, 'cached\_tokens': 0}.  

## Grok 3
Then I asked **Grok3 online** (I did not use DeepSearch).  It came up with a real article.  But when it came to the citations, instead of saying "Canadian Network for Mood and Anxiety Treatments..." it said "Canadian Network for Mood ***_bastards_*** Anxiety Treatments".  Weird!  I said "List references and citations" and it only listed the citation.

Any time I tried this, it gets actual articles 100% of the time.

---

## Claude
**Claude (3.7 Sonnet) cannot access, search for, or retrieve specific articles.**  So&mdash;it can tell us *about* certain things, but it can't give us the article it came from.

---

## Azure:

## gpt-35-turbo
"Do you have the ability to query the internet?"  
I don't have the ability to browse the internet or access real-time information. However, I can provide you with general information and answer questions based on the knowledge and data programmed into me.

## DeepSeek-R1
"Do you have the ability to query the internet?"  
I'm sorry, but currently I don't have access to the internet. Perhaps in the near future I'll have internet access to better serve you~

<br>
