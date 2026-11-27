% ==============================================================================
% nextmind-pdr.cls
% Custom LaTeX Document Class for Team NextMind — Fuel&Go Assignment 02 Report
% Status: Working v0.3.3 (Added needspace + FloatBarrier in \fgchapter — DEF-011/014)
% Engine: LuaLaTeX (fontspec)
% Backward-compatible with v0.1 (visual_sample.tex), v0.2 (visual_preview.tex), v0.3, v0.3.1, and v0.3.2
% ==============================================================================
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{nextmind-pdr}[2026/11/27 Working v0.3.3 (Team NextMind Fuel&Go PDR Class)]

\LoadClass[10pt,a4paper,oneside]{article}

% ------------------------------------------------------------------------------
% 1. Geometry & Page Layout
% ------------------------------------------------------------------------------
\RequirePackage[
  a4paper,
  top=22mm,
  bottom=20mm,
  left=20mm,
  right=20mm,
  headheight=20pt,
  headsep=7mm,
  footskip=10mm
]{geometry}

% ------------------------------------------------------------------------------
% 2. Typography (Portable fontspec with Documented TeX Gyre Fallbacks)
% ------------------------------------------------------------------------------
\RequirePackage{fontspec}
\defaultfontfeatures{Ligatures=TeX}
\RequirePackage[english,bidi=basic]{babel}
\babelprovide[import, onchar=ids fonts]{hebrew}

% Body & Sans: Calibri (Windows) with fallback to TeX Gyre Heros
\IfFontExistsTF{Calibri}{
  \setmainfont{Calibri}[
    BoldFont = {Calibri Bold},
    ItalicFont = {Calibri Italic},
    BoldItalicFont = {Calibri Bold Italic}
  ]
  \setsansfont{Calibri}[
    BoldFont = {Calibri Bold},
    ItalicFont = {Calibri Italic},
    BoldItalicFont = {Calibri Bold Italic}
  ]
}{
  \setmainfont{TeX Gyre Heros}
  \setsansfont{TeX Gyre Heros}
}

% Editorial Serif for Headings: Georgia (Windows) with fallback to TeX Gyre Pagella
\IfFontExistsTF{Georgia}{
  \newfontfamily\headingfont{Georgia}[
    BoldFont = {Georgia Bold},
    ItalicFont = {Georgia Italic},
    BoldItalicFont = {Georgia Bold Italic}
  ]
}{
  \newfontfamily\headingfont{TeX Gyre Pagella}
}

% Monospace for IDs, paths, endpoints: Consolas (Windows) with fallback to TeX Gyre Cursor
\IfFontExistsTF{Consolas}{
  \setmonofont{Consolas}[Scale=0.88]
}{
  \setmonofont{TeX Gyre Cursor}[Scale=0.90]
}

\RequirePackage{microtype}
\RequirePackage{setspace}
\setstretch{1.14}
\setlength{\parindent}{0pt}
\setlength{\parskip}{5pt}

% ------------------------------------------------------------------------------
% 3. Fuel&Go Adapted Visual Brief Color Palette (WCAG 2.1 AA Hardened)
%    Preserves all v0.1 color names + adds v0.2 semantic domain colors
% ------------------------------------------------------------------------------
\RequirePackage[table]{xcolor}

% Core Page & Ink (v0.1)
\definecolor{fgWhite}{HTML}{FFFFFF}
\definecolor{fgEspresso}{HTML}{403011}      % Primary ink & headings (12.74:1 on white)

% Brand Accents & Surfaces (v0.1)
\definecolor{fgOlive}{HTML}{626C3B}         % Primary accent & table header (5.63:1 w/ white)
\definecolor{fgOliveDark}{HTML}{4E572E}     % Deepened olive (7.70:1 w/ white)
\definecolor{fgCream}{HTML}{F6EBD4}         % Warm cream presentation surface
\definecolor{fgSoftCream}{HTML}{FAF4E6}     % Soft cream callout fill (11.61:1 w/ espresso)
\definecolor{fgPaleSage}{HTML}{EAEDDE}      % Pale sage callout/tint fill (10.71:1 w/ espresso)
\definecolor{fgAmber}{HTML}{E8AF3B}         % Golden amber graphical spine/accents ONLY
\definecolor{fgTextAmber}{HTML}{8C5A00}     % Darkened amber for kickers/links (5.87:1 on white)
\definecolor{fgOchre}{HTML}{83792E}         % Muted ochre chart/diagram series
\definecolor{fgSlateTeal}{HTML}{2E5E63}     % Slate teal chart series (v0.1 compat)
\definecolor{fgRuleGray}{HTML}{D8D2C5}      % Subtle warm divider rule

% Coordinated Semantic Domain Colors (v0.2)
\definecolor{fgTeal}{HTML}{1A565E}          % Deep Teal: digital platform / core architecture (8.21:1 on white)
\definecolor{fgTealTint}{HTML}{E6F0F2}      % Soft Teal tint surface (11.1:1 w/ espresso)
\definecolor{fgEcoGreen}{HTML}{2F6F4E}      % Fresh Sage/Eco Green: EV mobility (5.79:1 on white)
\definecolor{fgEcoTint}{HTML}{E7F2EC}       % Soft EV tint surface (11.3:1 w/ espresso)
\definecolor{fgTerracotta}{HTML}{B2562F}    % Restrained Terracotta: fuel forecourt (4.92:1 on white)
\definecolor{fgTerraTint}{HTML}{F9ECE6}     % Soft Fuel tint surface (11.0:1 w/ espresso)

\pagecolor{fgWhite}
\color{fgEspresso}

% ------------------------------------------------------------------------------
% 4. Core Packages (Graphics, Tables, Boxes, Diagrams, Links)
% ------------------------------------------------------------------------------
\RequirePackage{amsmath}
\RequirePackage{graphicx}
\RequirePackage{booktabs}
\RequirePackage{tabularx}
\RequirePackage{array}
\RequirePackage{enumitem}
\RequirePackage{fancyhdr}
\RequirePackage{titlesec}
\RequirePackage{caption}
\IfFileExists{placeins.sty}{\RequirePackage{placeins}}{\providecommand{\FloatBarrier}{\clearpage}}
\IfFileExists{needspace.sty}{\RequirePackage{needspace}}{\providecommand{\needspace}[1]{\par}}
\RequirePackage{tikz}
\usetikzlibrary{positioning,arrows.meta,shapes.geometric,calc,fit,backgrounds}
\RequirePackage[most]{tcolorbox}
\RequirePackage[
  colorlinks=true,
  linkcolor=fgTeal,
  citecolor=fgOlive,
  urlcolor=fgTextAmber
]{hyperref}

\captionsetup{
  font={small,color=fgEspresso},
  labelfont={bf,color=fgTeal},
  justification=raggedright,
  singlelinecheck=false,
  skip=5pt
}

% ------------------------------------------------------------------------------
% 5. Section Heading Hierarchy (Non-Hyphenated Georgia Editorial Serif)
% ------------------------------------------------------------------------------
\newcommand{\fg@nohyphen}{\raggedright\hyphenpenalty=10000\exhyphenpenalty=10000}

\titleformat{\section}
  {\fg@nohyphen\headingfont\Large\bfseries\color{fgEspresso}}
  {\textcolor{fgOlive}{\thesection.}}
  {0.5em}
  {}
  [\vspace{-2pt}\textcolor{fgAmber}{\rule{\linewidth}{1.1pt}}]
\titlespacing*{\section}{0pt}{10pt}{5pt}

\titleformat{\subsection}
  {\fg@nohyphen\headingfont\large\bfseries\color{fgTeal}}
  {\thesubsection}
  {0.5em}
  {}
\titlespacing*{\subsection}{0pt}{7pt}{3pt}

\titleformat{\subsubsection}
  {\fg@nohyphen\headingfont\normalsize\bfseries\color{fgEspresso}}
  {\thesubsubsection}
  {0.5em}
  {}
\titlespacing*{\subsubsection}{0pt}{5pt}{2pt}

% ------------------------------------------------------------------------------
% 6. Dynamic Running Header & Footer (lastpage deferred until final report)
% ------------------------------------------------------------------------------
\newcommand{\@fgRunningTitle}{Fuel\&Go --- Preliminary Design Report (Working v0.3)}
\newcommand{\@fgRunningMeta}{Team NextMind | Assignment 02}
\newcommand{\@fgRunningFooter}{Illustrative Visual Preview --- Provisional Class \texttt{nextmind-pdr.cls} v0.2 (Pending Q-04)}

\newcommand{\setrunningtitle}[1]{\renewcommand{\@fgRunningTitle}{#1}}
\newcommand{\setrunningmeta}[1]{\renewcommand{\@fgRunningMeta}{#1}}
\newcommand{\setrunningfooter}[1]{\renewcommand{\@fgRunningFooter}{#1}}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\footnotesize\textcolor{fgTeal}{\textbf{\@fgRunningTitle}}}
\fancyhead[R]{\footnotesize\textcolor{fgTextAmber}{\textbf{\@fgRunningMeta}}}
\renewcommand{\headrulewidth}{0.7pt}
\renewcommand{\headrule}{\hbox to\headwidth{\color{fgOlive}\leaders\hrule height \headrulewidth\hfill}}

\fancyfoot[L]{\footnotesize\textcolor{fgEspresso!75}{\@fgRunningFooter}}
% Total-page numbering (e.g., Page X of Y) is deferred until the final report build.
\fancyfoot[R]{\footnotesize\textcolor{fgEspresso}{\textbf{Page \thepage}}}
\renewcommand{\footrulewidth}{0.6pt}
\renewcommand{\footrule}{\hbox to\headwidth{\color{fgAmber}\leaders\hrule height \footrulewidth\hfill}}

% ------------------------------------------------------------------------------
% 7. Reusable Restrained TikZ Line Icons & Semantic Badges (v0.2)
% ------------------------------------------------------------------------------
% Inline Fuel Dispenser / Droplet Icon
\newcommand{\fgiconfuel}[1][fgTerracotta]{%
  \begin{tikzpicture}[baseline=-0.3ex, scale=0.22]
    \draw[#1, line width=0.9pt, rounded corners=0.6pt] (0,0) rectangle (1.1,1.55);
    \draw[#1, line width=0.7pt] (0.2,0.9) rectangle (0.9,1.35);
    \draw[#1, line width=0.8pt] (1.1,1.25) -- (1.45,1.25) -- (1.45,0.45) arc (180:360:0.16) -- (1.77,1.05) -- (1.6,1.35);
    \draw[#1, line width=0.9pt] (-0.15,0) -- (1.25,0);
  \end{tikzpicture}%
}

% Inline EV Charging Bolt Icon
\newcommand{\fgiconev}[1][fgEcoGreen]{%
  \begin{tikzpicture}[baseline=-0.3ex, scale=0.22]
    \draw[#1, line width=0.9pt] (0.95,1.6) -- (0.15,0.75) -- (0.72,0.75) -- (0.55,0.0) -- (1.45,0.92) -- (0.85,0.92) -- cycle;
  \end{tikzpicture}%
}

% Inline Core Platform Hub Icon
\newcommand{\fgiconcore}[1][fgTeal]{%
  \begin{tikzpicture}[baseline=-0.3ex, scale=0.22]
    \draw[#1, line width=0.9pt] (0.8,0.8) circle (0.72);
    \fill[#1] (0.8,0.8) circle (0.25);
    \draw[#1, line width=0.7pt] (0.8,1.52) -- (0.8,1.75) (0.8,0.08) -- (0.8,-0.15) (0.08,0.8) -- (-0.15,0.8) (1.52,0.8) -- (1.75,0.8);
  \end{tikzpicture}%
}

% Semantic Pill Badge: \fgbadge{bg}{fg}{solid|dashed}{label}
\newcommand{\fgbadge}[4]{%
  \tikz[baseline=(B.base)]{%
    \node[rectangle, rounded corners=2pt, fill=#1, draw=#2, #3, line width=0.65pt,
          inner xsep=4.5pt, inner ysep=2pt, font=\footnotesize\bfseries, text=#2] (B) {#4};
  }%
}

% ------------------------------------------------------------------------------
% 8. Distinctive Chapter-Opening Banner (v0.2)
% ------------------------------------------------------------------------------
\newcommand{\fgchapterbanner}[4]{%
  \noindent
  \begin{tikzpicture}
    \node[inner sep=0pt, anchor=north west] (box) at (0,0) {%
      \begin{minipage}{\linewidth}
        \begin{tabularx}{\linewidth}{@{}m{23mm} L@{}}
          \begin{tikzpicture}[x=1cm, y=1cm]
            \fill[fgCream, rounded corners=4pt] (0,0) rectangle (2.15,2.05);
            \draw[fgAmber, line width=1.1pt, rounded corners=4pt] (0,0) rectangle (2.15,2.05);
            % Subtle curved road arc motif
            \draw[fgTeal!30, line width=3pt] (0.15,0.28) .. controls (0.75,0.62) and (1.35,0.12) .. (2.0,0.45);
            \draw[fgWhite, dashed, line width=0.6pt] (0.18,0.28) .. controls (0.75,0.62) and (1.35,0.12) .. (1.97,0.45);
            \node[anchor=center, font=\headingfont\fontsize{24pt}{26pt}\selectfont\bfseries, text=fgTeal] at (1.075,1.30) {#1};
            \node[anchor=center, font=\tiny\bfseries, text=fgTextAmber] at (1.075,0.72) {CHAPTER};
          \end{tikzpicture}
          &
          {\fg@nohyphen
            \kicker{#2}\quad\fgiconfuel[fgTerracotta]\;\fgiconev[fgEcoGreen]\par
            \vspace{2pt}
            {\headingfont\fontsize{17pt}{20pt}\selectfont\bfseries\color{fgEspresso} #3\par}
            \vspace{2pt}
            {\small\color{fgOlive} #4\par}
          }
        \end{tabularx}
      \end{minipage}
    };
    \draw[fgTeal, line width=1.2pt] ($(box.south west)+(0,-3pt)$) -- ($(box.south east)+(0,-3pt)$);
    \draw[fgAmber, line width=1.2pt] ($(box.south west)+(0,-3pt)$) -- ($(box.south west)+(36mm,-3pt)$);
  \end{tikzpicture}
  \vspace{4pt}
}

% Integrated Numbered Chapter Banner + ToC Entry + Label (v0.3.3)
% Usage: \fgchapter{01}{Kicker}{Chapter Title}{Subtitle}{sec:label}
\newcommand{\fgchapter}[5]{%
  \FloatBarrier
  \needspace{10\baselineskip}%
  \refstepcounter{section}%
  \label{#5}%
  \addcontentsline{toc}{section}{\protect\numberline{\thesection}#3}%
  \fgchapterbanner{#1}{#2}{#3}{#4}%
  \par\nopagebreak
}

% Continuous-flow chapter banner (no forced \FloatBarrier/\clearpage; keeps \needspace)
\newcommand{\fgchapterflow}[5]{%
  \needspace{10\baselineskip}%
  \refstepcounter{section}%
  \label{#5}%
  \addcontentsline{toc}{section}{\protect\numberline{\thesection}#3}%
  \fgchapterbanner{#1}{#2}{#3}{#4}%
  \par\nopagebreak
}

% ------------------------------------------------------------------------------
% 9. Callout Cards, Insight Card & Decision Cards (v0.1 compat + v0.2)
% ------------------------------------------------------------------------------
% v0.1 Executive Callout (preserved)
\newtcolorbox{executivecallout}[1][Executive Highlight]{
  enhanced,
  breakable=false,
  colback=fgSoftCream,
  colframe=fgSoftCream,
  coltext=fgEspresso,
  borderline west={3.5pt}{0pt}{fgAmber},
  boxrule=0pt,
  arc=2pt,
  left=10pt,
  right=10pt,
  top=6pt,
  bottom=6pt,
  before skip=6pt,
  after skip=6pt,
  title={\textcolor{fgTextAmber}{\sffamily\footnotesize\bfseries\MakeUppercase{#1}}},
  colbacktitle=fgSoftCream,
  attach title to upper={\par\vspace{2pt}}
}

% v0.1 Sage Box (preserved)
\newtcolorbox{sagebox}[1][Technical Note]{
  enhanced,
  breakable=false,
  colback=fgPaleSage,
  colframe=fgPaleSage,
  coltext=fgEspresso,
  borderline west={3.5pt}{0pt}{fgOlive},
  boxrule=0pt,
  arc=2pt,
  left=10pt,
  right=10pt,
  top=6pt,
  bottom=6pt,
  before skip=6pt,
  after skip=6pt,
  title={\textcolor{fgOlive}{\sffamily\footnotesize\bfseries\MakeUppercase{#1}}},
  colbacktitle=fgPaleSage,
  attach title to upper={\par\vspace{2pt}}
}

% v0.1 Status Banner (preserved)
\newtcolorbox{statusbanner}{
  enhanced,
  breakable=false,
  colback=fgCream,
  colframe=fgAmber,
  coltext=fgEspresso,
  boxrule=1pt,
  arc=2pt,
  left=8pt,
  right=8pt,
  top=5pt,
  bottom=5pt,
  before skip=4pt,
  after skip=6pt
}

% v0.2 Refined Executive Insight Card
\newtcolorbox{insightcard}[1][Executive Insight]{
  enhanced,
  breakable=false,
  colback=fgSoftCream,
  colframe=fgRuleGray,
  coltext=fgEspresso,
  borderline west={4pt}{0pt}{fgTeal},
  boxrule=0.5pt,
  arc=3pt,
  left=11pt,
  right=11pt,
  top=7pt,
  bottom=7pt,
  before skip=6pt,
  after skip=7pt,
  title={\textcolor{fgTeal}{\sffamily\footnotesize\bfseries\MakeUppercase{#1}}},
  colbacktitle=fgSoftCream,
  attach title to upper={\par\vspace{2pt}}
}

% v0.2 Side-by-Side Illustrative Decision Card
% Usage: \fgdecisioncard{accentColor}{tintColor}{iconMacro}{kicker}{title}{body}
\newcommand{\fgdecisioncard}[6]{%
  \begin{tcolorbox}[
    enhanced,
    breakable=false,
    colback=#2,
    colframe=#1!45,
    coltext=fgEspresso,
    borderline north={2.5pt}{0pt}{#1},
    boxrule=0.5pt,
    arc=3pt,
    left=7pt,
    right=7pt,
    top=6pt,
    bottom=6pt,
    boxsep=1pt,
    height=38mm,
    valign=top
  ]
    {\scriptsize\bfseries\textcolor{#1}{#3\;#4}}\par
    \vspace{2pt}
    {\fg@nohyphen\headingfont\small\bfseries\color{fgEspresso} #5}\par
    \vspace{3pt}
    {\footnotesize #6}
  \end{tcolorbox}%
}

% ------------------------------------------------------------------------------
% 10. Table Styling Helpers (booktabs + tabularx + Olive/Teal Header)
% ------------------------------------------------------------------------------
\renewcommand{\arraystretch}{1.26}
\newcolumntype{L}{>{\raggedright\arraybackslash}X}
\newcolumntype{P}[1]{>{\raggedright\arraybackslash}p{#1}}
\newcommand{\fgtableheader}[1]{\textcolor{fgWhite}{\textbf{#1}}}
\newcommand{\kicker}[1]{\textcolor{fgTextAmber}{\footnotesize\bfseries\MakeUppercase{#1}}}

\endinput
