<script lang="ts">
	import TutorialRedirectButton from '../../../components/_TutorialRedirectButton.svelte';
	import AnimationContainer from '../../../components/AnimationContainer.svelte';
	import Footer from '../../../components/Footer.svelte';
	import Header from '../../../components/Header.svelte';
	import InformationTile from '../../../components/InformationTile.svelte';
	import QuoteCard from '../../../components/QuoteCard.svelte';
	import HistoricalCard from '../../../components/HistoricalCard.svelte';
	import OverviewSubCard from '../../../components/OverviewSubCard.svelte';
	import ApplicationCard from '../../../components/ApplicationCard.svelte';

	const redirects = [
		{ text: '1. Begriffsklärung', href: '#part-one', icon: 'terminal' },
		{ text: '2. Historische Entwicklung', href: '#part-two', icon: 'terminal' },
		{ text: '3. Arten von NLP', href: '#part-three', icon: 'terminal' },
		{ text: '4. Wichtige Konzepte', href: '#part-three', icon: 'terminal' },
		{ text: '5. Anwendungsgebiete', href: '#part-five', icon: 'terminal' }
	];
</script>

<Header />

<div class="flex flex-col  text-center justify-center items-center mt-20">
	<h1
		class="headline text-sm  sm:text-lg md:text-xl lg:text-3xl xl:text-5xl 2xl:text-6xl font-bold uppercase text-gray-100 [text-shadow:0_4px_8px_rgba(255,255,255,0.25)]"
	>
		Natural Language Processing
	</h1>
	<h2
		class="mt-2 mb-32 text-sm  sm:text-lg md:text-xl lg:text-3xl xl:text-4xl font-semibold text-gray-400 uppercase"
	>
		Von den Anfängen bis heute
	</h2>

	<div class="flex flex-col gap-10">
		{#each redirects as redirect, i}
			<AnimationContainer delay={i <= 5 ? String(i * 0.25) + 's' : '0s'}>
				<TutorialRedirectButton text={redirect.text} href={redirect.href} icon={redirect.icon} />
			</AnimationContainer>
		{/each}
	</div>
</div>

<div class="flex flex-col  mt-32 w-full">
	<div id="part-one" class="mt-32">
		<h1
			class="headline  text-2xl sm:text-3xl lg:text-4xl font-bold mb-12 ml-24 md:ml-18 lg:ml-24 uppercase text-gray-100"
		>
			1. Begriffsklärung
		</h1>

		<section
			class="flex flex-col place-content-start gap-16 mx-2 lg:mx-6 my-16 p-8 lg:p-16 text-center md:text-left shadow-lg rounded-md bg-cover"
			style="background-image: url(/background2.jpg)"
		>
			<QuoteCard
				img_link="/Hirschberg.jpg"
				img_source="https://datascience.columbia.edu/people/julia-hirschberg/"
				img_alt="Hirschberg"
				quote="NLP nutzt computergestützte Techniken - Algorithmen und statistische Analysen - zum Lernen,
				Verstehen und Produzieren von Inhalten in menschlicher Sprache."
				quote_source="https://www.engineering.columbia.edu/news/computer-scientists-julia-hirschberg-and-christopher-manning-discuss-natural-language-processing"
				position="justify-start"
				author="Julia Hirschberg"
				sub_content="Professorin für Informatik an der Columbia Universität"
			/>

			<QuoteCard
				img_link="/LaurenzWuttke.jpg"
				img_source="https://laurenzwuttke.com/ueber-laurenz-wuttke/"
				img_alt="Laurenz Wuttke"
				quote="Natural Language Processing (NLP) ist eine Methode der künstlichen Intelligenz,
				die es Computern ermöglicht, die natürliche Sprache des Menschen zu verstehen."
				quote_source="https://datasolut.com/natural-language-processing-einfuehrung/"
				position="justify-end"
				author="Laurenz Wuttke"
				sub_content="Experte für Marketingoptimierung durch KI und Gründer der datasolut GmbH."
			/>

			<QuoteCard
				img_link="/Elizabeth_Liddy.png"
				img_alt="Dr. Elizabeth D. Liddy"
				img_source="https://voice.daemen.edu/march-15-2021/alumni-profile-dr-elizabeth-d-liddy-66/"
				quote="Die Verarbeitung natürlicher Sprache ist eine theoretisch motivierte Reihe von Computertechniken
				zur Analyse und Darstellung natürlich vorkommender Texte auf einer oder mehreren Ebenen der Sprachanalyse,
				um eine menschenähnliche Sprachverarbeitung für eine Reihe von Aufgaben oder Anwendungen zu erreichen."
				quote_source="https://www.buchreport.de/news/it-was-ist-natural-language-processing/"
				position="justify-start"
				author="Dr. Elizabeth D. Liddy"
				sub_content="Informatikerin im Bereich von NLP"
			/>
		</section>

		<div class="flex flex-col justify-center items-center">
			<div class="flex flex-col mt-8 mb-28 justify-center items-center">
				<span
					class="text-base  sm:text-lg md:text-xl lg:text-2xl w-3/4 text-justify leading-relaxed mb-6 text-gray-300"
				>
					Natural Language Processing (NLP), zu deutsch Natürliche Sprachverarbeitung, ist eine
					Unterdisziplin des Bereichs der Künstlichen Intelligenz und mittlerweile genauso weit
					verbreitet. Mithilfe von NLP können riesige Datenmengen an Texten analysiert,
					Sprachassistenten oder Chatbots entwickelt werden. Im Gegensatz zu dem schwer definierbaren
					Begriff der "Künstlichen Intelligenz" kann bei NLP hingegen ziemlich exakt eingegrenzt
					werden, was damit gemeint ist. Dieser Artikel bietet einen Überblick über die wichtigsten
					Aspekte sowie die historische Entwicklung von NLP.
				</span>
			</div>
		</div>
	</div>

	<div id="part-two" class="mt-32">
		<h1
			class="headline w- text-2xl sm:text-3xl lg:text-4xl font-bold mb-12 ml-24 uppercase text-gray-100"
		>
			2. Historische Entwicklung
		</h1>

		<div class="flex flex-col items-center ml-[5%] w-[90%] sm:ml-0 sm:w-auto">
			<ol class="border-l-2 border-blue-600 w-[inherit] sm:w-[inherit]">
				<li>
					<HistoricalCard
						img_link="/grammar.jpg"
						img_alt="Grammar"
						source_link="https://mediax.stanford.edu/wp-content/uploads/2018/11/Rich_Dynamic_Treebank_Main.jpg"
						source_text="Quelle: DataVersity"
						heading="NLP Begins"
						content="1957 veröffentlichte Noam Chomsky ein Buch, in dem er frühere linguistische Konzepte revolutionierte und zu dem 
						Schluss kam, dass die Satzstruktur geändert werden müsste, damit ein Computer eine Sprache verstehen kann. Infolgedessen 
						schuf er einen neuen Grammatikstil namens Phasenstrukturgrammatik. Dieser Grammatikstil würde Sätze methodisch in ein 
						computerverständliches Format übersetzen."
						tag_list={['Noam CHomsky', 'Phrase-Structure Grammar']}
						button_link="https://www.dataversity.net/a-brief-history-of-natural-language-processing-nlp/#"
					/>
				</li>

				<li>
					<HistoricalCard
						img_link="/ELIZA_conversation.png"
						img_alt="Perzeptron"
						source_link="https://en.wikipedia.org/wiki/ELIZA#/media/File:ELIZA_conversation.png"
						source_text="Quelle: Wikipedia"
						heading="1964: Birth of ELIZA"
						content="1964 gründete der U.S. National Research Council (NRC) das Automatic Language Processing Advisory Committee oder ALPAC. 
						Dieses Komitee wurde beauftragt, den Fortschritt der Forschung zur Verarbeitung natürlicher Sprache zu bewerten.
						Im selben Jahr wurde ELIZA entwickelt, ein „maschinengeschriebener“ Kommentar- und Antwortprozess, der mithilfe von Reflexionstechniken 
						einen Psychiater imitieren sollte. Die Art und Weise, wie es seine Arbeit erledigte, bestand darin, Sätze neu anzuordnen und relativ 
						einfache Grammatikregeln zu befolgen, aber es gab kein Verständnis seitens des Computers.
						Nach einigen Jahren und Investitionen in Millionenhöhe galt die KI- und NLP-Forschung als tot."
						tag_list={['ELIZA', 'NRC']}
						button_link="https://en.wikipedia.org/wiki/ELIZA"
					/>
				</li>

				<li>
					<HistoricalCard
						img_link="/neural.png"
						img_alt="neural model"
						source_link="https://www.eidosmedia.com/blog/technology/machine-learning-size-isn-t-everything"
						source_text="Quelle: DataVersity"
						heading="Neural Net Models"
						content="Bis in die 1980er Jahre verwendeten die meisten NLP-Systeme komplexe, „handgeschriebene“ Regeln. Aber in den späten 1980er Jahren 
						kam es zu einer Revolution im NLP. Dies war sowohl das Ergebnis der stetigen Steigerung der Rechenleistung als auch der Umstellung auf 
						maschinelle Lernalgorithmen. In den 1980er Jahren war IBM für die Entwicklung mehrerer erfolgreicher, komplizierter statistischer Modelle 
						verantwortlich. Gegenwärtig gelten neuronale Netzmodelle als Spitzenreiter in Forschung und Entwicklung im NLP-Verständnis der Text- und Sprachgenerierung."
						tag_list={['neural net models', 'IBM']}
						button_link="https://www.dataversity.net/a-brief-history-of-natural-language-processing-nlp/#"
					/>
				</li>

				<li>
					<HistoricalCard
						img_link="/siri.webp"
						img_alt="Siri"
						source_link="https://mashable.com/article/how-to-set-up-siri"
						source_text="Quelle: DataVersity"
						heading="2000er: Spracherkennung"
						content="Apples Siri wurde 2011 als einer der weltweit ersten erfolgreichen NLP/KI-Assistenten bekannt, die von allgemeinen Verbrauchern verwendet wurden. 
						Innerhalb von Siri wandelt das Modul zur automatischen Spracherkennung die Wörter in digital interpretierte Konzepte um. Das Sprachbefehlssystem gleicht 
						diese Konzepte dann mit vordefinierten Befehlen ab und initiiert bestimmte Aktionen im Gerät. Trotz all dieser Verbesserungen sind unsere modernen KIs jedoch 
						immer noch nicht in der Lage, den Test von Alan Turing zu bestehen, und klingen derzeit nicht wie echte Menschen."
						tag_list={['Siri', 'Alan Turing']}
						button_link="https://www.dataversity.net/a-brief-history-of-natural-language-processing-nlp/#"
					/>
				</li>
			</ol>
		</div>
	</div>

	<div id="part-three" class="mt-32">
		<h1
			class="headline  text-2xl sm:text-3xl lg:text-4xl font-bold mb-12 ml-24 uppercase text-gray-100"
		>
			3. Arten von NLP
		</h1>
		<div class="flex flex-col mt-8 mb-28 justify-center items-center text-center">
			<span class="text-2xl w-3/4 leading-relaxed mb-6 text-gray-300 text-center">
				NLP selbst besteht aus zwei Unterkonzepten: Natural Language Understanding (NLU) und Natural
				Language Generation (NLG).
			</span>
		</div>

		<div class="flex flex-col w-[80%] sm:w-full ml-[10%] sm:ml-0 gap-y-60 items-center">
			<InformationTile title="Natural Language Understanding" class="mt-20">
				<div
					slot="content"
					class="text-gray-300 text-base sm:text-lg md:text-xl lg:text-2xl text-justify"
				>
					NLU ist eine Unterdisziplin von NLP, die noch präzisere syntaktische und semantische
					Analysen von Texten und Sprache nutzt, um die genaue Bedeutung eines Satzes zu verstehen.
					Die Syntax bezieht sich dabei auf die grammatikalische Struktur eines Satzes, während die
					Semantik auf die beabsichtigte Bedeutung verweist. Mithilfe von NLU ist es außerdem
					möglich, die Beziehungen zwischen Wörtern in einem Satz zu ermitteln. Dadurch können
					Wörter, die in manchen Sätzen als Nomen und in anderen als Adjektive auftreten durch den
					Kontext identifiziert und die korrekte Bedeutung des Satzes bestimmt werden.
				</div>
				<div slot="right_slot">
					<AnimationContainer from_right>
						<img src="/NLU.jpg" alt="vikus_viewer" class="rounded-3xl shadow-2xl" />
					</AnimationContainer>
				</div>
			</InformationTile>
			<InformationTile title="Natural Language Generation" right_side class="mt-20">
				<div
					slot="content"
					class="text-gray-300 text-base sm:text-lg md:text-xl lg:text-2xl text-justify"
				>
					NLG ist ebenfalls eine Unterdisziplin von NLP, bei der es, im Gegensatz zu NLU, nicht
					darum geht, die genaue Bedeutung eines Satzes zu verstehen. Vielmehr ist NLG der Prozess,
					bei dem auf der Grundlage einer Dateneingabe eine Textantwort in menschlicher Sprache
					erzeugt wird. Dieser Text kann zusätzlich noch durch text-to-speech-Dienste in ein
					Sprachformat umgewandelt werden. Diese Technologie kommt besonders bei Chatbots oder
					Sprachrobotern zum Einsatz, die Gespräche mit Menschen führen sollen.
				</div>
				<div slot="right_slot">
					<AnimationContainer>
						<img src="/NLG.jpg" alt="vikus_viewer" class="rounded-3xl shadow-2xl" />
					</AnimationContainer>
				</div>
			</InformationTile>
		</div>

		<section class="mb-32 mx-6 mt-48 text-gray-100 text-center bg-gray-800 rounded-2xl p-6">
			<div class="flex justify-center">
				<div class="text-center w-3/4 ">
					<h2 class=" text-2xl sm:text-3xl lg:text-4xl font-bold mb-6 text-center">
						Übersicht der wichtigsten NLP Konzepte
					</h2>
					<p class="text-2xl text-gray-400 mb-12">
						Hier wird auf einige wichtige Begriffe im Bereich von NLP eingegangen, die in ihrer
						Gesamtheit auch als Bestandteile der NLP-Pipeline bezeichnet werden.
					</p>
				</div>
			</div>

			<div
				class="grid bg-gray-700 gap-12 rounded-2xl shadow-2xl p-6 grid-cols-1 sm:grid-cols-1 md:grid-cols-2 xl:grid-cols-3 2xl:grid-cols-5 lg:gap-x-12"
			>
				<OverviewSubCard
					icon="tablet"
					icon_size="24px"
					heading="Tokenisierung"
					content="Tokenisierung beschreibt das Zerteilen eines Textes in seine Sätze und wenn benötigt,
					anschließend in einzelne Wörter, sogenannte Tokens. Die Umsetzung dessen ist bei den meisten
					europäischen Sprachen trivial, da man bei einem bestimmten Satzzeichen oder Leerzeichen separieren kann."
				/>

				<OverviewSubCard
					icon="slack"
					icon_size="24px"
					heading="Entfernen von Stop-Words"
					content="Sehr häufig auftretende Wörter, die keinen Inhalt besitzen, werden mithilfe von Listen,
					die diese Wörter enthalten, entfernt. Zu solchen Stop-Words zählen beispielsweise Artikel oder
					Präpositionen. Zuletzt bleiben nur noch für die Sprachverarbeitung relevante Wörter übrig."
				/>

				<OverviewSubCard
					icon="user"
					icon_size="24px"
					heading="Lemmatisierung"
					content="Mithilfe der Lemmatisierung sollen alle deklinierten Wörter auf ihre Grundform zurückgeführt werden.
					Bei dieser Technik wird mittels morphologischer Analyse und dem daraus resultierenden Kontextbezug auf die Basis,
					das Lemma, zurückgeführt."
				/>

				<OverviewSubCard
					icon="users"
					icon_size="24px"
					heading="POS Tagging"
					content="POS Tagging bzw. Part-of-Speech Tagging ordnet den einzelnen Bestandteilen eines Satzes die jeweilige
					Wortart (engl. Tag) zu. Für die weitere Sprachverarbeitung und semantische Analyse ist POS Tagging unabdingbar,
					da es eine Reihe von Wörtern gibt, die in verschiedenen Sätzen auch als unterschiedliche Wortart fungieren können.
					Mithilfe von POS Tagging können also Wörter in Sätzen klassifiziert und so zusätzliche Informationen gewonnen werden."
				/>

				<OverviewSubCard
					icon="file-text"
					icon_size="24px"
					heading="NER"
					content="NER (Named Entity Recognition) beschreibt das Kategorisieren wichtiger Substantive eines Satzes und basiert
					auf den Ergebnissen der Vorverarbeitung des Textes sowie dem POS Tagging. Mithilfe von NER können beispielsweise
					Fragen wie 'Welche Orte kommen in dem Text vor?' oder 'Welche Namen befinden sich in dem Satz?' beantwortet werden."
				/>
			</div>
		</section>
	</div>

	<div id="part-five" class="grid mt-32">
		<h1
			class="headline  text-2xl sm:text-3xl lg:text-4xl font-bold mb-12 ml-24 uppercase text-gray-100"
		>
			5. Anwendungsgebiete
		</h1>

		<div class="grid justify-center items-center justify-self-center w-3/4">
			<div
				class="grid gap-12 m-6 grid-cols-1 md:grid-cols-2 lg:grid-cols-2 xl:grid-cols-2 2xl:grid-cols-4"
			>
				<ApplicationCard
					img_source="/Suchmaschine.jpg"
					img_alt="Suchmaschine"
					heading="Suchmaschinen"
					content="Mithilfe von NLP ist es möglich, basierend auf der bisherigen Eingabe, konkrete
					Suchvorschläge anzubieten."
					read_more_link="https://kopfundstift.de/wie-funktioniert-eine-suchmaschine/"
				/>

				<ApplicationCard
					img_source="/Sprachassistenten.jpg"
					img_alt="Sprachassistenten"
					heading="Sprachassistenten"
					content="Sprachassistenten können die aufgenommenen Geräusche in Wörter übersetzen, diese mit
					natürlicher Sprachverarbeitung verstehen und so Aufgaben erfüllen."
					read_more_link="https://www.thisisdmg.com/wie-funktionieren-sprachassistenten/"
				/>

				<ApplicationCard
					img_source="/Chatbot.jpg"
					img_alt="Chatbot"
					heading="Chatbot"
					content="Besonders beim Kundenservice und -support setzen Unternehmen auf Chatbots, die alle
					auf NLP bzw. NLU und NLG basieren, um ein reales Gespräch mit dem Kunden zu simulieren."
					read_more_link="https://www.ibm.com/de-de/campaign/was-ist-ein-chatbot"
				/>

				<ApplicationCard
					img_source="/Content-Moderation.jpg"
					img_alt="Inhaltsverwaltung"
					heading="Inhaltsverwaltung"
					content="Die Inhaltsverwaltung in den sozialen Medien stellt die Anbieter vor große
					Herausforderungen. NLP Algorithmen können riesige Datenmengen an Texten analysieren und
					so anstößige Inhalte identifizieren."
					read_more_link="https://de.wikipedia.org/wiki/Content-Moderation"
				/>

				<ApplicationCard
					img_source="/Mobilität.jpg"
					img_alt="Mobilität"
					heading="Mobilität"
					content="Auch bei den Sprachassistenten in autonomen Fahrzeugen findet NLP Anwendung und unterstützt so den Fahrer."
					read_more_link="https://www.sueddeutsche.de/auto/verkehrssicherheit-so-weit-ist-das-autonome-fahren-1.3913983-2"
				/>
			</div>
		</div>
	</div>

	<div
		class="flex gap-16 w-full place-self-center items-center justify-center bg-gray-100 shadow-lg"
	>
		<div
			class="text-3xl font-sans leading-snug text-center font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-500 to-teal-500 drop-shadow-lg"
		>
			<h1>
				Support the <h1
					class="bg-clip-text text-transparent bg-gradient-to-r from-cyan-500 to-blue-500 drop-shadow-lg"
				>
					author!
				</h1>
			</h1>
		</div>
		<div class="flex flex-col md:flex-row md:max-w-xl ">
			<div class="w-auto text-center m-6 p-8">
				<img src="/Robert.jfif" class="rounded-full w-32 mb-4 mx-auto" alt="Avatar" />
				<h5 class="text-xl font-medium leading-tight mb-2">Robert Witzke</h5>
				<p class="text-gray-500 mb-2">Frontend Developer</p>
				<ul class="list-inside flex mx-auto justify-center">
					<a href="https://github.com/robertwitzke" class="px-2">
						<svg
							xmlns="http://www.w3.org/2000/svg"
							viewBox="0 0 496 512"
							class="w-4 h-4 text-blue-600"
						>
							<path
								fill="currentColor"
								d="M165.9 397.4c0 2-2.3 3.6-5.2 3.6-3.3.3-5.6-1.3-5.6-3.6 0-2 2.3-3.6 5.2-3.6 3-.3 5.6 1.3 5.6 3.6zm-31.1-4.5c-.7 2 1.3 4.3 4.3 4.9 2.6 1 5.6 0 6.2-2s-1.3-4.3-4.3-5.2c-2.6-.7-5.5.3-6.2 2.3zm44.2-1.7c-2.9.7-4.9 2.6-4.6 4.9.3 2 2.9 3.3 5.9 2.6 2.9-.7 4.9-2.6 4.6-4.6-.3-1.9-3-3.2-5.9-2.9zM244.8 8C106.1 8 0 113.3 0 252c0 110.9 69.8 205.8 169.5 239.2 12.8 2.3 17.3-5.6 17.3-12.1 0-6.2-.3-40.4-.3-61.4 0 0-70 15-84.7-29.8 0 0-11.4-29.1-27.8-36.6 0 0-22.9-15.7 1.6-15.4 0 0 24.9 2 38.6 25.8 21.9 38.6 58.6 27.5 72.9 20.9 2.3-16 8.8-27.1 16-33.7-55.9-6.2-112.3-14.3-112.3-110.5 0-27.5 7.6-41.3 23.6-58.9-2.6-6.5-11.1-33.3 2.6-67.9 20.9-6.5 69 27 69 27 20-5.6 41.5-8.5 62.8-8.5s42.8 2.9 62.8 8.5c0 0 48.1-33.6 69-27 13.7 34.7 5.2 61.4 2.6 67.9 16 17.7 25.8 31.5 25.8 58.9 0 96.5-58.9 104.2-114.8 110.5 9.2 7.9 17 22.9 17 46.4 0 33.7-.3 75.4-.3 83.6 0 6.5 4.6 14.4 17.3 12.1C428.2 457.8 496 362.9 496 252 496 113.3 383.5 8 244.8 8zM97.2 352.9c-1.3 1-1 3.3.7 5.2 1.6 1.6 3.9 2.3 5.2 1 1.3-1 1-3.3-.7-5.2-1.6-1.6-3.9-2.3-5.2-1zm-10.8-8.1c-.7 1.3.3 2.9 2.3 3.9 1.6 1 3.6.7 4.3-.7.7-1.3-.3-2.9-2.3-3.9-2-.6-3.6-.3-4.3.7zm32.4 35.6c-1.6 1.3-1 4.3 1.3 6.2 2.3 2.3 5.2 2.6 6.5 1 1.3-1.3.7-4.3-1.3-6.2-2.2-2.3-5.2-2.6-6.5-1zm-11.4-14.7c-1.6 1-1.6 3.6 0 5.9 1.6 2.3 4.3 3.3 5.6 2.3 1.6-1.3 1.6-3.9 0-6.2-1.4-2.3-4-3.3-5.6-2z"
							/>
						</svg>
					</a>
					<a href="https://www.linkedin.com/in/robert-witzke-1b1414244" class="px-2">
						<svg
							xmlns="http://www.w3.org/2000/svg"
							viewBox="0 0 448 512"
							class="w-4 h-4 text-blue-600"
						>
							<path
								fill="currentColor"
								d="M100.28 448H7.4V148.9h92.88zM53.79 108.1C24.09 108.1 0 83.5 0 53.8a53.79 53.79 0 0 1 107.58 0c0 29.7-24.1 54.3-53.79 54.3zM447.9 448h-92.68V302.4c0-34.7-.7-79.2-48.29-79.2-48.29 0-55.69 37.7-55.69 76.7V448h-92.78V148.9h89.08v40.8h1.3c12.4-23.5 42.69-48.3 87.88-48.3 94 0 111.28 61.9 111.28 142.3V448z"
							/>
						</svg>
					</a>
				</ul>
			</div>
			<div class="w-auto text-center m-6 p-8">
				<img src="/Hamid.jfif" class="rounded-full w-32 mb-4 mx-auto" alt="Avatar" />
				<h5 class="text-xl font-medium leading-tight mb-2">Hamid Omar</h5>
				<p class="text-gray-500 mb-2">Frontend Developer</p>
				<ul class="list-inside flex mx-auto justify-center">
					<a href="https://github.com/hamidomar000m" class="px-2">
						<svg
							xmlns="http://www.w3.org/2000/svg"
							viewBox="0 0 496 512"
							class="w-4 h-4 text-blue-600"
						>
							<path
								fill="currentColor"
								d="M165.9 397.4c0 2-2.3 3.6-5.2 3.6-3.3.3-5.6-1.3-5.6-3.6 0-2 2.3-3.6 5.2-3.6 3-.3 5.6 1.3 5.6 3.6zm-31.1-4.5c-.7 2 1.3 4.3 4.3 4.9 2.6 1 5.6 0 6.2-2s-1.3-4.3-4.3-5.2c-2.6-.7-5.5.3-6.2 2.3zm44.2-1.7c-2.9.7-4.9 2.6-4.6 4.9.3 2 2.9 3.3 5.9 2.6 2.9-.7 4.9-2.6 4.6-4.6-.3-1.9-3-3.2-5.9-2.9zM244.8 8C106.1 8 0 113.3 0 252c0 110.9 69.8 205.8 169.5 239.2 12.8 2.3 17.3-5.6 17.3-12.1 0-6.2-.3-40.4-.3-61.4 0 0-70 15-84.7-29.8 0 0-11.4-29.1-27.8-36.6 0 0-22.9-15.7 1.6-15.4 0 0 24.9 2 38.6 25.8 21.9 38.6 58.6 27.5 72.9 20.9 2.3-16 8.8-27.1 16-33.7-55.9-6.2-112.3-14.3-112.3-110.5 0-27.5 7.6-41.3 23.6-58.9-2.6-6.5-11.1-33.3 2.6-67.9 20.9-6.5 69 27 69 27 20-5.6 41.5-8.5 62.8-8.5s42.8 2.9 62.8 8.5c0 0 48.1-33.6 69-27 13.7 34.7 5.2 61.4 2.6 67.9 16 17.7 25.8 31.5 25.8 58.9 0 96.5-58.9 104.2-114.8 110.5 9.2 7.9 17 22.9 17 46.4 0 33.7-.3 75.4-.3 83.6 0 6.5 4.6 14.4 17.3 12.1C428.2 457.8 496 362.9 496 252 496 113.3 383.5 8 244.8 8zM97.2 352.9c-1.3 1-1 3.3.7 5.2 1.6 1.6 3.9 2.3 5.2 1 1.3-1 1-3.3-.7-5.2-1.6-1.6-3.9-2.3-5.2-1zm-10.8-8.1c-.7 1.3.3 2.9 2.3 3.9 1.6 1 3.6.7 4.3-.7.7-1.3-.3-2.9-2.3-3.9-2-.6-3.6-.3-4.3.7zm32.4 35.6c-1.6 1.3-1 4.3 1.3 6.2 2.3 2.3 5.2 2.6 6.5 1 1.3-1.3.7-4.3-1.3-6.2-2.2-2.3-5.2-2.6-6.5-1zm-11.4-14.7c-1.6 1-1.6 3.6 0 5.9 1.6 2.3 4.3 3.3 5.6 2.3 1.6-1.3 1.6-3.9 0-6.2-1.4-2.3-4-3.3-5.6-2z"
							/>
						</svg>
					</a>
					<a href="https://www.linkedin.com/in/hamid-omar-229452187" class="px-2">
						<svg
							xmlns="http://www.w3.org/2000/svg"
							viewBox="0 0 448 512"
							class="w-4 h-4 text-blue-600"
						>
							<path
								fill="currentColor"
								d="M100.28 448H7.4V148.9h92.88zM53.79 108.1C24.09 108.1 0 83.5 0 53.8a53.79 53.79 0 0 1 107.58 0c0 29.7-24.1 54.3-53.79 54.3zM447.9 448h-92.68V302.4c0-34.7-.7-79.2-48.29-79.2-48.29 0-55.69 37.7-55.69 76.7V448h-92.78V148.9h89.08v40.8h1.3c12.4-23.5 42.69-48.3 87.88-48.3 94 0 111.28 61.9 111.28 142.3V448z"
							/>
						</svg>
					</a>
				</ul>
			</div>
		</div>
	</div>
</div>

<Footer />

<style lang="postcss">
</style>
