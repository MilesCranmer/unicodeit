# Copyright (c) 2010 Sven Kreiss, Kyle Cranmer
from __future__ import unicode_literals
__author__ = "Sven Kreiss <sk@svenkreiss.com>, Kyle Cranmer <kyle.cranmer@nyu.edu>"
__version__ = "0.6.2"
import sys, re
import six

replacements = [
    (r'\\textfractionsolidus', '\u2044'),
    (r'\\leftrightsquigarrow', '\u21AD'),
    (r'\\textpertenthousand', '\u2031'),
    (r'\\blacktriangleright', '\u25B8'),
    (r'\\blacktriangledown', '\u25BE'),
    (r'\\blacktriangleleft', '\u25C2'),
    (r'\\twoheadrightarrow', '\u21A0'),
    (r'\\leftrightharpoons', '\u21CB'),
    (r'\\rightleftharpoons', '\u21CC'),
    (r'\\textreferencemark', '\u203B'),
    (r'\\circlearrowright', '\u21BB'),
    (r'\\rightrightarrows', '\u21C9'),
    (r'\\vartriangleright', '\u22B3'),
    (r'\\textordmasculine', '\u00BA'),
    (r'\\textvisiblespace', '\u2423'),
    (r'\\twoheadleftarrow', '\u219E'),
    (r'\\downharpoonright', '\u21C2'),
    (r'\\ntrianglerighteq', '\u22ED'),
    (r'\\rightharpoondown', '\u21C1'),
    (r'\\textperthousand', '\u2030'),
    (r'\\leftrightarrows', '\u21C6'),
    (r'\\textmusicalnote', '\u266A'),
    (r'\\nleftrightarrow', '\u21AE'),
    (r'\\rightleftarrows', '\u21C4'),
    (r'\\bigtriangledown', '\u25BD'),
    (r'\\textordfeminine', '\u00AA'),
    (r'\\ntrianglelefteq', '\u22EC'),
    (r'\\rightthreetimes', '\u22CC'),
    (r'\\trianglerighteq', '\u22B5'),
    (r'\\vartriangleleft', '\u22B2'),
    (r'\\rightsquigarrow', '\u21DD'),
    (r'\\downharpoonleft', '\u21C3'),
    (r'\\curvearrowright', '\u21B7'),
    (r'\\circlearrowleft', '\u21BA'),
    (r'\\leftharpoondown', '\u21BD'),
    (r'\\nLeftrightarrow', '\u21CE'),
    (r'\\curvearrowleft', '\u21B6'),
    (r'\\guilsinglright', '\u203A'),
    (r'\\leftthreetimes', '\u22CB'),
    (r'\\leftrightarrow', '\u2194'),
    (r'\\rightharpoonup', '\u21C0'),
    (r'\\guillemotright', '\u00BB'),
    (r'\\downdownarrows', '\u21CA'),
    (r'\\hookrightarrow', '\u21AA'),
    (r'\\hspace\{0\.25em\}', '\u2005'),
    (r'\\dashrightarrow', '\u21E2'),
    (r'\\leftleftarrows', '\u21C7'),
    (r'\\trianglelefteq', '\u22B4'),
    (r'\\ntriangleright', '\u22EB'),
    (r'\\doublebarwedge', '\u2306'),
    (r'\\upharpoonright', '\u21BE'),
    (r'\\rightarrowtail', '\u21A3'),
    (r'\\looparrowright', '\u21AC'),
    (r'\\Leftrightarrow', '\u21D4'),
    (r'\\sphericalangle', '\u2222'),
    (r'\\divideontimes', '\u22C7'),
    (r'\\measuredangle', '\u2221'),
    (r'\\blacktriangle', '\u25B4'),
    (r'\\ntriangleleft', '\u22EA'),
    (r'\\mathchar"1356', '\u2041'),
    (r'\\texttrademark', '\u2122'),
    (r'\\mathchar"2208', '\u2316'),
    (r'\\triangleright', '\u25B9'),
    (r'\\leftarrowtail', '\u21A2'),
    (r'\\guilsinglleft', '\u2039'),
    (r'\\upharpoonleft', '\u21BF'),
    (r'\\mathbb\{gamma\}', '\u213D'),
    (r'\\fallingdotseq', '\u2252'),
    (r'\\looparrowleft', '\u21AB'),
    (r'\\textbrokenbar', '\u00A6'),
    (r'\\hookleftarrow', '\u21A9'),
    (r'\\smallsetminus', '\uFE68'),
    (r'\\dashleftarrow', '\u21E0'),
    (r'\\guillemotleft', '\u00AB'),
    (r'\\leftharpoonup', '\u21BC'),
    (r'\\mathbb\{Gamma\}', '\u213E'),
    (r'\\bigtriangleup', '\u25B3'),
    (r'\\textcircledP', '\u2117'),
    (r'\\risingdotseq', '\u2253'),
    (r'\\triangleleft', '\u25C3'),
    (r'\\mathsterling', '\u00A3'),
    (r'\\textcurrency', '\u00A4'),
    (r'\\triangledown', '\u25BF'),
    (r'\\blacklozenge', '\uE80B'),
    (r'\\sfrac\{5\}\{6\}', '\u215A'),
    (r'\\preccurlyeq', '\u227C'),
    (r'\\Rrightarrow', '\u21DB'),
    (r'\\circledcirc', '\u229A'),
    (r'\\nRightarrow', '\u21CF'),
    (r'\\sfrac\{3\}\{8\}', '\u215C'),
    (r'\\sfrac\{1\}\{3\}', '\u2153'),
    (r'\\sfrac\{2\}\{5\}', '\u2156'),
    (r'\\vartriangle', '\u25B5'),
    (r'\\Updownarrow', '\u21D5'),
    (r'\\nrightarrow', '\u219B'),
    (r'\\sfrac\{1\}\{2\}', '\u00BD'),
    (r'\\sfrac\{3\}\{5\}', '\u2157'),
    (r'\\succcurlyeq', '\u227D'),
    (r'\\sfrac\{4\}\{5\}', '\u2158'),
    (r'\\diamondsuit', '\u2666'),
    (r'\\hphantom\{0\}', '\u2007'),
    (r'\\sfrac\{1\}\{6\}', '\u2159'),
    (r'\\curlyeqsucc', '\u22DF'),
    (r'\\blacksquare', '\u25AA'),
    (r'\\hphantom\{,\}', '\u2008'),
    (r'\\curlyeqprec', '\u22DE'),
    (r'\\sfrac\{1\}\{8\}', '\u215B'),
    (r'\\sfrac\{7\}\{8\}', '\u215E'),
    (r'\\sfrac\{1\}\{5\}', '\u2155'),
    (r'\\sfrac\{2\}\{3\}', '\u2154'),
    (r'\\updownarrow', '\u2195'),
    (r'\\backepsilon', '\u220D'),
    (r'\\circleddash', '\u229D'),
    (r'\\eqslantless', '\u22DC'),
    (r'\\sfrac\{3\}\{4\}', '\u00BE'),
    (r'\\sfrac\{5\}\{8\}', '\u215D'),
    (r'\\hspace\{1pt\}', '\u200A'),
    (r'\\sfrac\{1\}\{4\}', '\u00BC'),
    (r'\\mathbb\{Pi\}', '\u213F'),
    (r'\\mathcal\{M\}', '\u2133'),
    (r'\\mathcal\{o\}', '\u02134'),
    (r'\\mathcal\{O\}', '\u1D4AA'),
    (r'\\nsupseteqq', '\u2289'),
    (r'\\mathcal\{B\}', '\u212C'),
    (r'\\textrecipe', '\u211E'),
    (r'\\nsubseteqq', '\u2288'),
    (r'\\subsetneqq', '\u228A'),
    (r'\\mathcal\{I\}', '\u2111'),
    (r'\\upuparrows', '\u21C8'),
    (r'\\mathcal\{e\}', '\u212F'),
    (r'\\mathcal\{L\}', '\u2112'),
    (r'\\nleftarrow', '\u219A'),
    (r'\\mathcal\{H\}', '\u210B'),
    (r'\\mathcal\{E\}', '\u2130'),
    (r'\\eqslantgtr', '\u22DD'),
    (r'\\curlywedge', '\u22CF'),
    (r'\\varepsilon', '\u03B5'),
    (r'\\supsetneqq', '\u228B'),
    (r'\\rightarrow', '\u2192'),
    (r'\\mathcal\{R\}', '\u211B'),
    (r'\\sqsubseteq', '\u2291'),
    (r'\\mathcal\{g\}', '\u210A'),
    (r'\\sqsupseteq', '\u2292'),
    (r'\\complement', '\u2201'),
    (r'\\Rightarrow', '\u21D2'),
    (r'\\gtreqqless', '\u22DB'),
    (r'\\lesseqqgtr', '\u22DA'),
    (r'\\circledast', '\u229B'),
    (r'\\nLeftarrow', '\u21CD'),
    (r'\\Lleftarrow', '\u21DA'),
    (r'\\Leftarrow', '\u21D0'),
    (r'\\gvertneqq', '\u2269'),
    (r'\\mathbb\{C\}', '\u2102'),
    (r'\\supsetneq', '\u228B'),
    (r'\\leftarrow', '\u2190'),
    (r'\\nleqslant', '\u2270'),
    (r'\\mathbb\{Q\}', '\u211A'),
    (r'\\mathbb\{Z\}', '\u2124'),
    (r'\\llbracket', '\u301A'),
    (r'\\mathbb\{H\}', '\u210D'),
    (r'\\spadesuit', '\u2660'),
    (r'\\mathit\{o\}', '\u2134'),
    (r'\\mathbb\{P\}', '\u2119'),
    (r'\\rrbracket', '\u301B'),
    (r'\\supseteqq', '\u2287'),
    (r'\\copyright', '\u00A9'),
    (r'\\textsc\{k\}', '\u0138'),
    (r'\\gtreqless', '\u22DB'),
    (r'\\mathbb\{j\}', '\u2149'),
    (r'\\pitchfork', '\u22D4'),
    (r'\\estimated', '\u212E'),
    (r'\\ngeqslant', '\u2271'),
    (r'\\mathbb\{e\}', '\u2147'),
    (r'\\therefore', '\u2234'),
    (r'\\triangleq', '\u225C'),
    (r'\\varpropto', '\u221D'),
    (r'\\subsetneq', '\u228A'),
    (r'\\heartsuit', '\u2665'),
    (r'\\mathbb\{d\}', '\u2146'),
    (r'\\lvertneqq', '\u2268'),
    (r'\\checkmark', '\u2713'),
    (r'\\nparallel', '\u2226'),
    (r'\\mathbb\{R\}', '\u211D'),
    (r'\\lesseqgtr', '\u22DA'),
    (r'\\downarrow', '\u2193'),
    (r'\\mathbb\{D\}', '\u2145'),
    (r'\\mathbb\{i\}', '\u2148'),
    (r'\\backsimeq', '\u22CD'),
    (r'\\mathbb\{N\}', '\u2115'),
    (r'\\Downarrow', '\u21D3'),
    (r'\\subseteqq', '\u2286'),
    (r'\\setminus', '\u2216'),
    (r'\\succnsim', '\u22E9'),
    (r'\\doteqdot', '\u2251'),
    (r'\\clubsuit', '\u2663'),
    (r'\\emptyset', '\u2205'),
    (r'\\varnothing', '\u2205'),
    (r'\\sqsupset', '\u2290'),
    (r'\\fbox\{~~\}', '\u25AD'),
    (r'\\curlyvee', '\u22CE'),
    (r'\\varkappa', '\u03F0'),
    (r'\\llcorner', '\u231E'),
    (r'\\varsigma', '\u03C2'),
    (r'\\approxeq', '\u224A'),
    (r'\\backcong', '\u224C'),
    (r'\\supseteq', '\u2287'),
    (r'\\circledS', '\u24C8'),
    (r'\\circledR', '\u00AE'),
    (r'\\textcent', '\u00A2'),
    (r'\\urcorner', '\u231D'),
    (r'\\lrcorner', '\u231F'),
    (r'\\boxminus', '\u229F'),
    (r'\\texteuro', '\u20AC'),
    (r'\\vartheta', '\u03D1'),
    (r'\\barwedge', '\u22BC'),
    (r'\\ding\{86\}', '\u2736'),
    (r'\\sqsubset', '\u228F'),
    (r'\\subseteq', '\u2286'),
    (r'\\intercal', '\u22BA'),
    (r'\\ding\{73\}', '\u2606'),
    (r'\\ulcorner', '\u231C'),
    (r'\\recorder', '\u2315'),
    (r'\\precnsim', '\u22E8'),
    (r'\\parallel', '\u2225'),
    (r'\\boxtimes', '\u22A0'),
    (r'\\ding\{55\}', '\u2717'),
    (r'\\multimap', '\u22B8'),
    (r'\\maltese', '\u2720'),
    (r'\\nearrow', '\u2197'),
    (r'\\swarrow', '\u2199'),
    (r'\\lozenge', '\u25CA'),
    (r'\\sqrt\[3\]', '\u221B'),
    (r'\\succsim', '\u227F'),
    (r'\\tilde\{\}', '\u007E'),
    (r'\\lessgtr', '\u2276'),
    (r'\\Upsilon', '\u03D2'),
    (r'\\Cdprime', '\u042A'),
    (r'\\gtrless', '\u2277'),
    (r'\\backsim', '\u223D'),
    (r'\\nexists', '\u2204'),
    (r'\\dotplus', '\u2214'),
    (r'\\searrow', '\u2198'),
    (r'\\lessdot', '\u22D6'),
    (r'\\boxplus', '\u229E'),
    (r'\\upsilon', '\u03C5'),
    (r'\\epsilon', '\u03B5'),
    (r'\\diamond', '\u22C4'),
    (r'\\bigstar', '\u2605'),
    (r'\\ddagger', '\u2021'),
    (r'\\cdprime', '\u044A'),
    (r'\\Uparrow', '\u21D1'),
    (r'\\sqrt\[4\]', '\u221C'),
    (r'\\between', '\u226C'),
    (r'\\sqangle', '\u221F'),
    (r'\\digamma', '\u03DC'),
    (r'\\uparrow', '\u2191'),
    (r'\\nwarrow', '\u2196'),
    (r'\\precsim', '\u227E'),
    (r'\\breve\{\}', '\u02D8'),
    (r'\\because', '\u2235'),
    (r'\\bigcirc', '\u25EF'),
    (r'\\acute\{\}', '\u00B4'),
    (r'\\grave\{\}', '\u0060'),
    (r'\\check\{\}', '\u02C7'),
    (r'\\lesssim', '\u2272'),
    (r'\\partial', '\u2202'),
    (r'\\natural', '\u266E'),
    (r'\\supset', '\u2283'),
    (r'\\hstrok', '\u0127'),
    (r'\\Tstrok', '\u0166'),
    (r'\\coprod', '\u2210'),
    (r'\\models', '\u22A7'),
    (r'\\otimes', '\u2297'),
    (r'\\degree', '\u00B0'),
    (r'\\gtrdot', '\u22D7'),
    (r'\\preceq', '\u227C'),
    (r'\\Lambda', '\u039B'),
    (r'\\lambda', '\u03BB'),
    (r'\\cprime', '\u044C'),
    (r'\\varrho', '\u03F1'),
    (r'\\Bumpeq', '\u224E'),
    (r'\\hybull', '\u2043'),
    (r'\\lmidot', '\u0140'),
    (r'\\nvdash', '\u22AC'),
    (r'\\lbrace', '\u007B'),
    (r'\\bullet', '\u2022'),
    (r'\\varphi', '\u03D5'),
    (r'\\bumpeq', '\u224F'),
    (r'\\ddot\{\}', '\u00A8'),
    (r'\\Lmidot', '\u013F'),
    (r'\\Cprime', '\u042C'),
    (r'\\female', '\u2640'),
    (r'\\rtimes', '\u22CA'),
    (r'\\gtrsim', '\u2273'),
    (r'\\mapsto', '\u21A6'),
    (r'\\daleth', '\u2138'),
    (r'\\square', '\u25A0'),
    (r'\\nVDash', '\u22AF'),
    (r'\\rangle', '\u3009'),
    (r'\\tstrok', '\u0167'),
    (r'\\oslash', '\u2298'),
    (r'\\ltimes', '\u22C9'),
    (r'\\lfloor', '\u230A'),
    (r'\\marker', '\u25AE'),
    (r'\\Subset', '\u22D0'),
    (r'\\Vvdash', '\u22AA'),
    (r'\\propto', '\u221D'),
    (r'\\Hstrok', '\u0126'),
    (r'\\dlcrop', '\u230D'),
    (r'\\forall', '\u2200'),
    (r'\\nVdash', '\u22AE'),
    (r'\\Supset', '\u22D1'),
    (r'\\langle', '\u3008'),
    (r'\\ominus', '\u2296'),
    (r'\\rfloor', '\u230B'),
    (r'\\circeq', '\u2257'),
    (r'\\eqcirc', '\u2256'),
    (r'\\drcrop', '\u230C'),
    (r'\\veebar', '\u22BB'),
    (r'\\ulcrop', '\u230F'),
    (r'\\nvDash', '\u22AD'),
    (r'\\urcrop', '\u230E'),
    (r'\\exists', '\u2203'),
    (r'\\approx', '\u2248'),
    (r'\\dagger', '\u2020'),
    (r'\\boxdot', '\u22A1'),
    (r'\\succeq', '\u227D'),
    (r'\\bowtie', '\u22C8'),
    (r'\\subset', '\u2282'),
    (r'\\Sigma', '\u03A3'),
    (r'\\Omega', '\u03A9'),
    (r'\\nabla', '\u2207'),
    (r'\\colon', '\u003A'),
    (r'\\boxHu', '\u2567'),
    (r'\\boxHd', '\u2564'),
    (r'\\aleph', '\u2135'),
    (r'\\gnsim', '\u22E7'),
    (r'\\boxHU', '\u2569'),
    (r'\\boxHD', '\u2566'),
    (r'\\equiv', '\u2261'),
    (r'\\lneqq', '\u2268'),
    (r'\\alpha', '\u03B1'),
    (r'\\amalg', '\u2210'),
    (r'\\boxhU', '\u2568'),
    (r'\\boxhD', '\u2565'),
    (r'\\uplus', '\u228E'),
    (r'\\boxhu', '\u2534'),
    (r'\\kappa', '\u03BA'),
    (r'\\sigma', '\u03C3'),
    (r'\\boxDL', '\u2557'),
    (r'\\Theta', '\u0398'),
    (r'\\Vdash', '\u22A9'),
    (r'\\boxDR', '\u2554'),
    (r'\\boxDl', '\u2556'),
    (r'\\sqcap', '\u2293'),
    (r'\\boxDr', '\u2553'),
    (r'\\bar\{\}', '\u00AF'),
    (r'\\dashv', '\u22A3'),
    (r'\\vDash', '\u22A8'),
    (r'\\boxdl', '\u2510'),
    (r'\\boxVl', '\u2562'),
    (r'\\boxVh', '\u256B'),
    (r'\\boxVr', '\u255F'),
    (r'\\boxdr', '\u250C'),
    (r'\\boxdL', '\u2555'),
    (r'\\boxVL', '\u2563'),
    (r'\\boxVH', '\u256C'),
    (r'\\boxVR', '\u2560'),
    (r'\\boxdR', '\u2552'),
    (r'\\theta', '\u03B8'),
    (r'\\lhblk', '\u2584'),
    (r'\\uhblk', '\u2580'),
    (r'\\ldotp', '\u002E'),
    (r'\\ldots', '\u2026'),
    (r'\\boxvL', '\u2561'),
    (r'\\boxvH', '\u256A'),
    (r'\\boxvR', '\u255E'),
    (r'\\boxvl', '\u2524'),
    (r'\\boxvh', '\u253C'),
    (r'\\boxvr', '\u251C'),
    (r'\\Delta', '\u0394'),
    (r'\\boxUR', '\u255A'),
    (r'\\boxUL', '\u255D'),
    (r'\\oplus', '\u2295'),
    (r'\\boxUr', '\u2559'),
    (r'\\boxUl', '\u255C'),
    (r'\\doteq', '\u2250'),
    (r'\\happy', '\u32E1'),
    (r'\\varpi', '\u03D6'),
    (r'\\boxr', '\u2514'),
    (r'\\smile', '\u263A'),
    (r'\\boxul', '\u2518'),
    (r'\\simeq', '\u2243'),
    (r'\\boxuR', '\u2558'),
    (r'\\boxuL', '\u255B'),
    (r'\\boxhd', '\u252C'),
    (r'\\gimel', '\u2137'),
    (r'\\Gamma', '\u0393'),
    (r'\\lnsim', '\u22E6'),
    (r'\\sqcup', '\u2294'),
    (r'\\omega', '\u03C9'),
    (r'\\sharp', '\u266F'),
    (r'\\times', '\u00D7'),
    (r'\\block', '\u2588'),
    (r'\\hat\{\}', '\u005E'),
    (r'\\wedge', '\u2227'),
    (r'\\vdash', '\u22A2'),
    (r'\\angle', '\u2220'),
    (r'\\infty', '\u221E'),
    (r'\\gamma', '\u03B3'),
    (r'\\asymp', '\u224D'),
    (r'\\rceil', '\u2309'),
    (r'\\dot\{\}', '\u02D9'),
    (r'\\lceil', '\u2308'),
    (r'\\delta', '\u03B4'),
    (r'\\gneqq', '\u2269'),
    (r'\\frown', '\u2322'),
    (r'\\phone', '\u260E'),
    (r'\\vdots', '\u22EE'),
    (r'\\k\{i\}', '\u012F'),
    (r'\\`\{I\}', '\u00CC'),
    (r'\\perp', '\u22A5'),
    (r'\\"\{o\}', '\u00F6'),
    (r'\\=\{I\}', '\u012A'),
    (r'\\`\{a\}', '\u00E0'),
    (r'\\v\{T\}', '\u0164'),
    (r'\\surd', '\u221A'),
    (r'\\H\{O\}', '\u0150'),
    (r'\\vert', '\u007C'),
    (r'\\k\{I\}', '\u012E'),
    (r'\\"\{y\}', '\u00FF'),
    (r'\\"\{O\}', '\u00D6'),
    (r'\\\'\{Y\}', '\u00DD'),
    (r'\\u\{u\}', '\u045E'),
    (r'\\u\{G\}', '\u011E'),
    (r'\\\.\{E\}', '\u0116'),
    (r'\\\.\{z\}', '\u017C'),
    (r'\\v\{t\}', '\u0165'),
    (r'\\prec', '\u227A'),
    (r'\\H\{o\}', '\u0151'),
    (r'\\mldr', '\u2026'),
    (r'\\\'\{y\}', '\u00FD'),
    (r'\\cong', '\u2245'),
    (r'\\\.\{e\}', '\u0117'),
    (r'\\\'\{L\}', '\u0139'),
    (r'\\star', '\u002A'),
    (r'\\\.\{Z\}', '\u017B'),
    (r'\\\'\{e\}', '\u00E9'),
    (r'\\geqq', '\u2267'),
    (r'\\cdot', '\u22C5'),
    (r'\\`\{U\}', '\u00D9'),
    (r'\\\'\{l\}', '\u013A'),
    (r'\\v\{L\}', '\u013D'),
    (r'\\c\{s\}', '\u015F'),
    (r'\\\'\{s\}', '\u015B'),
    (r'\\~\{A\}', '\u00C3'),
    (r'\\Vert', '\u2016'),
    (r'\\k\{e\}', '\u0119'),
    (r'\\lnot', '\u00AC'),
    (r'\\\'\{z\}', '\u017A'),
    (r'\\leqq', '\u2266'),
    (r'\\beta', '\u03B2'),
    (r'\\beth', '\u2136'),
    (r'\\\'\{E\}', '\u00C9'),
    (r'\\~\{n\}', '\u00F1'),
    (r'\\u\{i\}', '\u0439'),
    (r'\\c\{S\}', '\u015E'),
    (r'\\c\{N\}', '\u0145'),
    (r'\\H\{u\}', '\u0171'),
    (r'\\v\{n\}', '\u0148'),
    (r'\\\'\{S\}', '\u015A'),
    (r'\\=\{U\}', '\u016A'),
    (r'\\~\{O\}', '\u00D5'),
    (r'\\\'\{Z\}', '\u0179'),
    (r'\\v\{E\}', '\u011A'),
    (r'\\\'\{R\}', '\u0154'),
    (r'\\H\{U\}', '\u0170'),
    (r'\\v\{N\}', '\u0147'),
    (r'\\prod', '\u220F'),
    (r'\\v\{s\}', '\u0161'),
    (r'\\"\{U\}', '\u00DC'),
    (r'\\c\{n\}', '\u0146'),
    (r'\\k\{U\}', '\u0172'),
    (r'\\c\{R\}', '\u0156'),
    (r'\\\'\{A\}', '\u00C1'),
    (r'\\~\{o\}', '\u00F5'),
    (r'\\v\{e\}', '\u011B'),
    (r'\\v\{S\}', '\u0160'),
    (r'\\u\{A\}', '\u0102'),
    (r'\\circ', '\u2218'),
    (r'\\"\{u\}', '\u00FC'),
    (r'\\flat', '\u266D'),
    (r'\\v\{z\}', '\u017E'),
    (r'\\r\{U\}', '\u016E'),
    (r'\\`\{O\}', '\u00D2'),
    (r'\\=\{u\}', '\u016B'),
    (r'\\oint', '\u222E'),
    (r'\\c\{K\}', '\u0136'),
    (r'\\k\{u\}', '\u0173'),
    (r'\\not<', '\u226E'),
    (r'\\not>', '\u226F'),
    (r'\\`\{o\}', '\u00F2'),
    (r'\\"\{I\}', '\u00CF'),
    (r'\\v\{D\}', '\u010E'),
    (r'\\\.\{G\}', '\u0120'),
    (r'\\r\{u\}', '\u016F'),
    (r'\\not=', '\u2260'),
    (r'\\`\{u\}', '\u00F9'),
    (r'\\v\{c\}', '\u010D'),
    (r'\\c\{k\}', '\u0137'),
    (r'\\\.\{g\}', '\u0121'),
    (r'\\\'\{N\}', '\u0143'),
    (r'\\odot', '\u2299'),
    (r'\\`\{e\}', '\u044D'),
    (r'\\c\{T\}', '\u0162'),
    (r'\\v\{d\}', '\u010F'),
    (r'\\"\{e\}', '\u0451'),
    (r'\\\'\{I\}', '\u00CD'),
    (r'\\v\{R\}', '\u0158'),
    (r'\\k\{a\}', '\u0105'),
    (r'\\nldr', '\u2025'),
    (r'\\`\{A\}', '\u00C0'),
    (r'\\\'\{n\}', '\u0144'),
    (r'\\~\{N\}', '\u00D1'),
    (r'\\nmid', '\u2224'),
    (r'\\\.\{C\}', '\u010A'),
    (r'\\zeta', '\u03B6'),
    (r'\\~\{u\}', '\u0169'),
    (r'\\`\{E\}', '\u042D'),
    (r'\\~\{a\}', '\u00E3'),
    (r'\\c\{t\}', '\u0163'),
    (r'\\=\{o\}', '\u014D'),
    (r'\\v\{r\}', '\u0159'),
    (r'\\=\{A\}', '\u0100'),
    (r'\\\.\{c\}', '\u010B'),
    (r'\\~\{U\}', '\u0168'),
    (r'\\k\{A\}', '\u0104'),
    (r'\\"\{a\}', '\u00E4'),
    (r'\\u\{U\}', '\u040E'),
    (r'\\iota', '\u03B9'),
    (r'\\=\{O\}', '\u014C'),
    (r'\\c\{C\}', '\u00C7'),
    (r'\\gneq', '\u2269'),
    (r'\\\'\{c\}', '\u0107'),
    (r'\\boxH', '\u2550'),
    (r'\\hbar', '\u210F'),
    (r'\\"\{A\}', '\u00C4'),
    (r'\\boxv', '\u2502'),
    (r'\\boxh', '\u2500'),
    (r'\\male', '\u2642'),
    (r'\\\'\{u\}', '\u00FA'),
    (r'\\sqrt', '\u221A'),
    (r'\\succ', '\u227B'),
    (r'\\c\{c\}', '\u00E7'),
    (r'\\\'\{C\}', '\u0106'),
    (r'\\v\{l\}', '\u013E'),
    (r'\\u\{a\}', '\u0103'),
    (r'\\v\{Z\}', '\u017D'),
    (r'\\\'\{o\}', '\u00F3'),
    (r'\\c\{G\}', '\u0122'),
    (r'\\v\{C\}', '\u010C'),
    (r'\\lneq', '\u2268'),
    (r'\\"\{E\}', '\u0401'),
    (r'\\=\{a\}', '\u0101'),
    (r'\\c\{l\}', '\u013C'),
    (r'\\\'\{a\}', '\u00E1'),
    (r'\\=\{E\}', '\u0112'),
    (r'\\boxV', '\u2551'),
    (r'\\u\{g\}', '\u011F'),
    (r'\\\'\{O\}', '\u00D3'),
    (r'\\\'\{g\}', '\u01F5'),
    (r'\\u\{I\}', '\u0419'),
    (r'\\c\{L\}', '\u013B'),
    (r'\\k\{E\}', '\u0118'),
    (r'\\\.\{I\}', '\u0130'),
    (r'\\~\{I\}', '\u0128'),
    (r'\\quad', '\u2003'),
    (r'\\c\{r\}', '\u0157'),
    (r'\\\'\{r\}', '\u0155'),
    (r'\\"\{Y\}', '\u0178'),
    (r'\\=\{e\}', '\u0113'),
    (r'\\\'\{U\}', '\u00DA'),
    (r'\\leq', '\u2264'),
    (r'\\Cup', '\u22D3'),
    (r'\\Psi', '\u03A8'),
    (r'\\neq', '\u2260'),
    (r'\\k\{\}', '\u02DB'),
    (r'\\=\{\}', '\u203E'),
    (r'\\H\{\}', '\u02DD'),
    (r'\\cup', '\u222A'),
    (r'\\geq', '\u2265'),
    (r'\\mho', '\u2127'),
    (r'\\Dzh', '\u040F'),
    (r'\\cap', '\u2229'),
    (r'\\bot', '\u22A5'),
    (r'\\psi', '\u03C8'),
    (r'\\chi', '\u03C7'),
    (r'\\c\{\}', '\u00B8'),
    (r'\\Phi', '\u03A6'),
    (r'\\ast', '\u002A'),
    (r'\\ell', '\u2113'),
    (r'\\top', '\u22A4'),
    (r'\\lll', '\u22D8'),
    (r'\\tau', '\u03C4'),
    (r'\\Cap', '\u22D2'),
    (r'\\sad', '\u2639'),
    (r'\\iff', '\u21D4'),
    (r'\\eta', '\u03B7'),
    (r'\\eth', '\u00F0'),
    (r'\\d\{\}', '\u0323'),
    (r'\\rho', '\u03C1'),
    (r'\\dzh', '\u045F'),
    (r'\\div', '\u00F7'),
    (r'\\phi', '\u03C6'),
    (r'\\Rsh', '\u21B1'),
    (r'\\vee', '\u2228'),
    (r'\\b\{\}', '\u02CD'),
    (r'\\t\{\}', '\u0361'),
    (r'\\int', '\u222B'),
    (r'\\sim', '\u223C'),
    (r'\\r\{\}', '\u02DA'),
    (r'\\Lsh', '\u21B0'),
    (r'\\yen', '\u00A5'),
    (r'\\ggg', '\u22D9'),
    (r'\\mid', '\u2223'),
    (r'\\sum', '\u2211'),
    (r'\\Dz', '\u0405'),
    (r'\\Re', '\u211C'),
    (r'\\oe', '\u0153'),
    (r'\\DH', '\u00D0'),
    (r'\\ll', '\u226A'),
    (r'\\ng', '\u014B'),
    (r'\\\'G', '\u0403'),
    (r'\\wr', '\u2240'),
    (r'\\wp', '\u2118'),
    (r'\\=I', '\u0406'),
    (r'\\:\)', '\u263A'),
    (r'\\:\(', '\u2639'),
    (r'\\AE', '\u00C6'),
    (r'\\AA', '\u00C5'),
    (r'\\ss', '\u00DF'),
    (r'\\dz', '\u0455'),
    (r'\\ae', '\u00E6'),
    (r'\\aa', '\u00E5'),
    (r'\\th', '\u00FE'),
    (r'\\to', '\u2192'),
    (r'\\Pi', '\u03A0'),
    (r'\\mp', '\u2213'),
    (r'\\Im', '\u2111'),
    (r'\\pm', '\u00B1'),
    (r'\\pi', '\u03C0'),
    (r'\\"I', '\u0407'),
    (r'\\\'C', '\u040B'),
    (r'\\in', '\u2208'),
    (r'\\\'K', '\u040C'),
    (r'\\\'k', '\u045C'),
    (r'\\\'c', '\u045B'),
    (r'\\\'g', '\u0453'),
    (r'\\ni', '\u220B'),
    (r'\\ne', '\u2260'),
    (r'\\TH', '\u00DE'),
    (r'\\Xi', '\u039E'),
    (r'\\nu', '\u03BD'),
    (r'\\NG', '\u014A'),
    (r'\\:G', '\u32E1'),
    (r'\\xi', '\u03BE'),
    (r'\\OE', '\u0152'),
    (r'\\gg', '\u226B'),
    (r'\\DJ', '\u0110'),
    (r'\\=e', '\u0454'),
    (r'\\=E', '\u0404'),
    (r'\\mu', '\u03BC'),
    (r'\\dj', '\u0111'),
    (r'\\:', '\u2004'),
    (r'\\;', '\u2002'),
    (r'\\&', '\u0026'),
    (r'\\\$', '\u0024'),
    (r'\\%', '\u0025'),
    (r'\\#', '\u0023'),
    (r'\\,', '\u2009'),
    (r'\\-', '\u00AD'),
    (r'\\S', '\u00A7'),
    (r'\\P', '\u00B6'),
    (r'\\O', '\u00D8'),
    (r'\\L', '\u0141'),
    (r'\\\}', '\u007D'),
    (r'\\o', '\u00F8'),
    (r'\\l', '\u0142'),
    (r'\\h', '\u210E'),
    (r'\\i', '\u2139'),
]
combiningmarks = [
    (r'\\tilde', '\u0303'),
    (r'\\grave', '\u0300'),
    (r'\\dot', '\u0307'),
    (r'\\acute', '\u0301'),
    (r'\\doubleunderline', '\u0333'),
    (r'\\ddot', '\u0308'),
    (r'\\slash', '\u0338'),
    (r'\\overline', '\u0305'),
    (r'\\vec', '\u20D7'),
    (r'\\hat', '\u0302'),
    (r'\\breve', '\u0306'),
    (r'\\underline', '\u0332'),
    (r'\\strikethrough', '\u0335'),
    (r'\\bar', '\u0305'),
]
subsuperscripts = [
    (r'_x', '\u2093'),
    (r'_v', '\u1D65'),
    (r'_u', '\u1D64'),
    (r'_t', '\u209C'),
    (r'_s', '\u209B'),
    (r'_r', '\u1D63'),
    (r'_p', '\u209A'),
    (r'_o', '\u2092'),
    (r'_n', '\u2099'),
    (r'_m', '\u2098'),
    (r'_l', '\u2097'),
    (r'_k', '\u2096'),
    (r'_j', '\u2C7C'),
    (r'_i', '\u1D62'),
    (r'_h', '\u2095'),
    (r'_e', '\u2091'),
    (r'_a', '\u2090'),
    (r'\^\u222B', '\u1DB4'),
    (r'_>', '\u02F2'),
    (r'_=', '\u208C'),
    (r'_<', '\u02F1'),
    (r'_9', '\u2089'),
    (r'_8', '\u2088'),
    (r'_7', '\u2087'),
    (r'_6', '\u2086'),
    (r'_5', '\u2085'),
    (r'_4', '\u2084'),
    (r'_3', '\u2083'),
    (r'_2', '\u2082'),
    (r'_1', '\u2081'),
    (r'_0', '\u2080'),
    (r'_-', '\u208B'),
    (r'_\+', '\u208A'),
    (r'_\)', '\u208E'),
    (r'_\(', '\u208D'),
    (r'_\u03C1', '\u1D68'),
    (r'_\u03C7', '\u1D6A'),
    (r'_\u03C6', '\u1D69'),
    (r'_\u03B2', '\u1D66'),
    (r'_\u03B3', '\u1D67'),
    (r'\^\u03C6', '\u1D60'),
    (r'\^\u03C7', '\u1D61'),
    (r'\^\u03B4', '\u1D5F'),
    (r'\^\u03B3', '\u1D5E'),
    (r'\^\u03B2', '\u1D5D'),
    (r'\^8', '\u2078'),
    (r'\^9', '\u2079'),
    (r'\^<', '\u02C2'),
    (r'\^=', '\u207C'),
    (r'\^>', '\u02C3'),
    (r'\^0', '\u2070'),
    (r'\^1', '\u00B9'),
    (r'\^2', '\u00B2'),
    (r'\^3', '\u00B3'),
    (r'\^4', '\u2074'),
    (r'\^5', '\u2075'),
    (r'\^6', '\u2076'),
    (r'\^7', '\u2077'),
    (r'\^\(', '\u207D'),
    (r'\^\)', '\u207E'),
    (r'\^\*', '\u002A'),
    (r'\^\+', '\u207A'),
    (r'\^-', '\u207B'),
    (r'\^P', '\u1D3E'),
    (r'\^R', '\u1D3F'),
    (r'\^T', '\u1D40'),
    (r'\^U', '\u1D41'),
    (r'\^V', '\u1111'),
    (r'\^W', '\u1D42'),
    (r'\^H', '\u1D34'),
    (r'\^I', '\u1D35'),
    (r'\^J', '\u1D36'),
    (r'\^K', '\u1D37'),
    (r'\^L', '\u1D38'),
    (r'\^M', '\u1D39'),
    (r'\^N', '\u1D3A'),
    (r'\^O', '\u1D3C'),
    (r'\^A', '\u1D2C'),
    (r'\^B', '\u1D2E'),
    (r'\^D', '\u1D30'),
    (r'\^E', '\u1D31'),
    (r'\^G', '\u1D33'),
    (r'\^x', '\u02E3'),
    (r'\^y', '\u02B8'),
    (r'\^z', '\u1DBB'),
    (r'\^p', '\u1D56'),
    (r'\^r', '\u02B3'),
    (r'\^s', '\u02E2'),
    (r'\^t', '\u1D57'),
    (r'\^u', '\u1D58'),
    (r'\^v', '\u1D5B'),
    (r'\^w', '\u02B7'),
    (r'\^h', '\u02B0'),
    (r'\^i', '\u2071'),
    (r'\^j', '\u02B2'),
    (r'\^k', '\u1D4F'),
    (r'\^l', '\u02E1'),
    (r'\^m', '\u1D50'),
    (r'\^n', '\u207F'),
    (r'\^o', '\u1D52'),
    (r'\^a', '\u1D43'),
    (r'\^b', '\u1D47'),
    (r'\^c', '\u1D9C'),
    (r'\^d', '\u1D48'),
    (r'\^e', '\u1D49'),
    (r'\^f', '\u1DA0'),
    (r'\^g', '\u1D4D'),
]


def replace(inp):
    result = []
    for f in inp:
        f = six.text_type(f)
        
        #f = re.sub(r"([^\\])([_|\^])", r"\1\\\2", f) # do not require backslash in front of ^ or _
        #f = re.sub(r"^([_|\^])", r"\\\1", f)
        
        # escape combining marks with a space after the backslash
        for c in combiningmarks:
            offset = 0
            for s in re.finditer(c[0], f):
                f = f[:s.start()+1+offset] + " " + f[s.start()+1+offset:]
                offset += 1
            
        for r in replacements:
            f = re.sub(r[0], r[1], f)

        # expand groups of subscripts: \_{01234}    
        offset = 0
        #for s in re.finditer(r"\\_\{[^\}]+\}", f):
        for s in re.finditer(r"_\{[0-9\+-=\(\)<>\-aeoxjhklmnpstiruv\u03B2\u03B3\u03C1\u03C6\u03C7]+\}", f):
            newstring,n = re.subn(r"([0-9\+-=\(\)<>\-aeoxjhklmnpstiruv\u03B2\u03B3\u03C1\u03C6\u03C7])", r"_\1", s.group(0)[2:-1])
            f = f[:s.start()+offset] + newstring + f[s.end()+offset:]
            offset += n*2 - (n + 3)
            
            
        # expand groups of superscripts: \^{01234}    
        offset = 0
        #for s in re.finditer(r"\\\^\{[^\}]+\}", f):
        for s in re.finditer(r"\^\{[0-9\+-=\(\)<>ABDEGHIJKLMNOPRTUWabcdefghijklmnoprstuvwxyz\u03B2\u03B3\u03B4\u03C6\u03C7\u222B]+\}", f):
            newstring,n = re.subn(r"([0-9\+-=\(\)<>ABDEGHIJKLMNOPRTUWabcdefghijklmnoprstuvwxyz\u03B2\u03B3\u03B4\u03C6\u03C7\u222B])", r"^\1", s.group(0)[2:-1])
            f = f[:s.start()+offset] + newstring + f[s.end()+offset:]
            offset += n*2 - (n + 3)
        
        # now replace subsuperscripts
        for r in subsuperscripts:
            f = re.sub(r[0], r[1], f)

        # combining marks (unicode char modifies previous char)
        for c in combiningmarks:
            offset = 0
            for s in re.finditer(r"\\ "+c[0][2:]+r"\{[^\}]+\}", f):
                newstring,n = re.subn(r"(.)", r"\1"+c[1], s.group(0)[len(c[0])+1:-1])
                f = f[:s.start()+offset] + newstring + f[s.end()+offset:]
                offset += n - (n + len(c[0])+1)

        result.append( six.text_type(f).encode("utf-8") )
                
    return result


if __name__ == "__main__":
    result = replace(sys.argv[1:])
    def print_no_b(data):
        if not isinstance(data, str):
            data = data.decode()
        print(data)
    for r in result: print_no_b(r)
