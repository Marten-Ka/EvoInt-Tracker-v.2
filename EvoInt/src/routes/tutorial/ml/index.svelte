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
		{ text: '3. Arten von ML', href: '#part-three', icon: 'terminal' },
		{ text: '4. Wichtige Begriffe', href: '#part-three', icon: 'terminal' },
		{ text: '5. Anwendungsgebiete', href: '#part-five', icon: 'terminal' }
	];
</script>

<Header />

<div class="flex flex-col  text-center justify-center items-center mt-20">
	<h1
		class="headline text-sm  sm:text-lg md:text-xl lg:text-3xl xl:text-5xl 2xl:text-6xl font-bold uppercase text-gray-100 [text-shadow:0_4px_8px_rgba(255,255,255,0.25)]"
	>
		Machine Learning
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
				img_link="/ibm.svg"
				img_source="https://www.ibm.com/design/language/877b208e9d05b37650a70e55867861bd/core_gray60_on_white.svg"
				img_alt="IBM Cloud Education"
				quote="Maschinelles Lernen, Machine Learning (ML), ist ein Zweig der künstlichen
				Intelligenz (KI) und Computerwissenschaft, der sich auf die Verwendung von Daten
				und Algorithmen konzentriert, um die Art und Weise, wie Menschen lernen, zu
				imitieren und die Genauigkeit schrittweise zu verbessern."
				quote_source="https://www.ibm.com/de-de/cloud/learn/machine-learning"
				position="justify-start"
				author="IBM Cloud Education"
			/>

			<QuoteCard
				img_link="/AndrewNg.webp"
				img_source="https://www.andrewng.org/static/c5eb39b8da664718384eefcbc915f5cd/25582/andrew-ng-homepage.webp"
				img_alt="Andrew Ng"
				quote="Maschinelles Lernen ist die Wissenschaft, Computer zum Handeln zu bringen, ohne
				explizit programmiert zu werden"
				quote_source="http://mlclass.stanford.edu/#:~:text=Machine%20learning%20is%20the%20science,understanding%20of%20the%20human%20genome."
				position="justify-end"
				author="Andrew Ng"
				sub_content="Direktor des Labors für künstliche Intelligenz in Stanford"
			/>

			<QuoteCard
				img_link="/MichaelWooldridge.jpg"
				img_alt="Michael Wooldridge"
				img_source="https://www.cs.ox.ac.uk/files/8605//PTAIT_20161031_0020%20%282%29.jpg"
				quote="Maschinelles Lernen zielt darauf ab, Computer zu bauen, die lernen können,
				Entscheidungen zu treffen oder Aufgaben auszuführen, ohne dass ihnen explizit
				gesagt wird, wie sie das tun sollen"
				quote_source="https://www.cs.ox.ac.uk/research/ai_ml/"
				position="justify-start"
				author="Michael Wooldridge"
				sub_content="Professor für Informatik an der Universität Oxford"
			/>
		</section>

		<div class="flex flex-col justify-center items-center">
			<div class="flex flex-col mt-8 mb-28 justify-center items-center">
				<span
					class="text-base  sm:text-lg md:text-xl lg:text-2xl w-3/4 text-justify leading-relaxed mb-6 text-gray-300"
				>
					Machine Learning, auf Deutsch: Machinelles Lernen, ist heute für viele Organisationen ein
					notwendiger Aspekt der modernen Geschäftswelt und Forschung. Es verwendet Algorithmen und
					neuronale Netzwerkmodelle, um Computersysteme bei der schrittweisen Verbesserung ihrer
					Leistung zu unterstützen. Diese Seite soll dazu dienen, einen Überblick rund um das Thema
					ML zu schaffen - von den Anfängen bis zur heutigen Zeit.
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
						img_link="/samuel.jpeg"
						img_alt="Samuel"
						source_link="https://medium.com/ibm-data-ai/the-first-of-its-kind-ai-model-samuels-checkers-playing-program-1b712fa4ab96"
						source_text="Quelle: Micro Medium"
						heading="1952: Samuel's Checker Player"
						content="Arthur Samuel von IBM entwickelte 1952 ein Computerprogramm zum Damespiel für den
						IBM 701. Sein Entwurf beinhaltete eine Punktefunktion, die die Positionen der
						Figuren auf dem Brett nutzte. Die Bewertungsfunktion versuchte, die Gewinnchancen
						jeder Seite zu messen. Samuel entwarf auch eine Reihe von Mechanismen, die es ihm
						ermöglichten, sein Programm zu verbessern. Bei dem, was Samuel Auswendiglernen
						nannte, erinnerte sich sein Programm an alle Positionen, die es bereits gesehen
						hatte, und kombinierte dies mit den Werten der Belohnungsfunktion. 1952 prägte
						Arthur Samuel erstmals den Begriff „Machine Learning“."
						tag_list={['Arthur Samuel', 'Grundstein der ML']}
						button_link="https://webdocs.cs.ualberta.ca/~jonathan/publications/ai_publications/samuel.pdf"
					/>
				</li>

				<li>
					<HistoricalCard
						img_link="/perceptron.gif"
						img_alt="Perzeptron"
						source_link="https://medium.com/towards-data-science/what-the-hell-is-perceptron-626217814f53"
						source_text="Quelle: Medium"
						heading="1957: Der Perzeptron"
						content="1957 schuf Frank Rosenblatt Perzeptron, indem er Donald Hebbs Modell der
						Gehirnzellinteraktion mit Arthur Samuels Bemühungen um Machine Learining
						kombinierte. Das Perzeptron war ursprünglich als Maschine geplant, nicht als
						Programm. Die Software wurde ursprünglich für den IBM 704 entwickelt und in einer
						speziell angefertigten Maschine namens Mark 1 Perceptron installiert, die für die
						Bilderkennung konstruiert worden war. Dadurch wurden die Software und die
						Algorithmen übertragbar und für andere Maschinen verfügbar. Obwohl das Perzeptron
						vielversprechend schien, konnte es viele Arten von visuellen Mustern nicht
						erkennen, was zu Frustration führte und die Erforschung neuronaler Netzwerke
						blockierte. Es hat bei den Investoren zu Frustration geführt und Finanzierungen
						wurden zurückgenommen."
						tag_list={['Bilderkennung', 'Frank Rosenblatt']}
						button_link="https://de.wikipedia.org/wiki/Perzeptron"
					/>
				</li>

				<li>
					<HistoricalCard
						img_link="/neighbor.png"
						img_alt="Neighbor"
						source_link="https://towardsdatascience.com/similarity-search-with-ivfpq-9c6348fd4db3"
						source_text="Quelle: Towards Data Science"
						heading="1967: Der Nearest Neighbor Algorithmus"
						content="1967 wurde der Beginn der grundlegenden Mustererkennung durch die Konzeption des
						Nearest-Neighbor-Algorithmus erreicht. Marcello Pelillo ist berühmt geworden, weil
						er die „Nearest-Neighbor-Regel“ erfunden hat. Dieser Algorithmus wurde zur
						Kartierung von Routen verwendet und war einer der frühesten Algorithmen, die
						verwendet wurden, um eine Lösung für das Problem des Handlungsreisenden zu finden,
						die effizienteste Route zu finden. Unter Verwendung dieser gibt ein Verkäufer eine
						ausgewählte Stadt ein und lässt das Programm wiederholt die nächstgelegenen Städte
						besuchen, bis alle besucht wurden."
						tag_list={['Marcello Pelillo', 'Der Nearest-Neighbour-Algorithmus']}
						button_link="https://de.wikipedia.org/wiki/Nearest-Neighbor-Heuristik"
					/>
				</li>

				<li>
					<HistoricalCard
						img_link="/aiki.png"
						img_alt="AI vs KI"
						source_link="https://towardsai.net/p/machine-learning/differences-between-ai-and-machine-learning-1255b182fc6"
						source_text="Quelle: Towards AI"
						heading="1970er: KI und ML trennen sich"
						content="In den späten 1970er und frühen 1980er Jahren konzentrierte sich die Forschung im
						Bereich der künstlichen Intelligenz mehr auf die Verwendung logischer,
						wissensbasierter Ansätze als auf Algorithmen, und die Erforschung neuronaler
						Netzwerke wurde von Informatik- und KI-Forschern aufgegeben. Dies führte zu einer
						Spaltung zwischen KI und Machine Learning, welche bis dahin als Trainingsprogramm
						für KI verwendet wurde. Das Ziel der ML-Industrie verlagerte sich von der
						Ausbildung für künstliche Intelligenz zur Lösung praktischer Probleme, wobei die
						ML-Industrie ihren Fokus auf neuronale Netze behielt und dann in den 1990er Jahren
						florierte. Der größte Teil dieses Erfolgs war auf das Wachstum des Internets
						zurückzuführen, das von der ständig wachsenden Verfügbarkeit digitaler Daten und
						der Möglichkeit profitierte, seine Dienste über das Internet zu teilen."
						tag_list={['Künstliche Intelligenz', 'Machine Learning']}
						button_link="https://towardsai.net/p/machine-learning/differences-between-ai-and-machine-learning-1255b182fc6"
					/>
				</li>

				<li>
					<HistoricalCard
						img_link="/boosting.jpg"
						img_alt="Boosting"
						source_link="https://www.ecmwf.int/sites/default/files/Ai-image-deep-net-v3-690px.jpg"
						source_text="Quelle: ECMWF"
						heading="1990: Boosting-Algorithmen"
						content="Boosting-Algorithmen reduzieren Vorurteile während des Supervised Learning und
						beinhalten ML-Algorithmen, die schwache Lernende in starke verwandeln. Dieses
						Konzept wurde erstmals 1990 in einem Artikel mit dem Titel „The Strength of Weak
						Learnability“ von Robert Schapire vorgestellt. Schapire argumentiert: „Eine Gruppe
						schwacher Lernender kann einen einzigen starken Lernenden hervorbringen.“ wobei
						schwache Lernende als Klassifikatoren definiert werden, die nur geringfügig mit
						der wahren Klassifikation korrelieren, und ein starker Lernender leicht
						klassifiziert und gut auf die wahre Klassifikation ausgerichtet ist. „Boosting“
						gilt als notwendige Weiterentwicklung für die Evolution des maschinellen Lernens."
						tag_list={['Supervised Learning', 'Robert Schapire']}
						button_link="https://de.wikipedia.org/wiki/Boosting#:~:text=Boosting%20(engl.,einem%20einzigen%20guten%20Klassifikator%20verschmilzt."
					/>
				</li>

				<li>
					<HistoricalCard
						img_link="/speechrecog.jpg"
						img_alt="Spracherkennung"
						source_link="https://recfaces.com/articles/what-is-voice-recognition"
						source_text="Quelle: Recfaces"
						heading="1997: Spracherkennungssysteme"
						content="1997 beschrieben Jürgen Schmidhuber und Sepp Hochreite ein neuronales
						Netzwerkmodell namens Long Short-Term Memory (LSTM), das derzeit zum Trainieren
						vieler Spracherkennungssysteme verwendet wird. LSTM kann Aufgaben lernen, die die
						Erinnerung an Ereignisse erfordern, die Tausende von diskreten Schritten zuvor
						stattgefunden haben. Im Jahr 2015 hatte das Spracherkennungsprogramm von Google
						Berichten zufolge einen signifikanten Leistungssprung von 49 Prozent, indem es ein
						von Connectionist Temporal Classification (CTC) trainiertes LSTM verwendete, eine
						Art neuronaler Netzwerkausgabe und Bewertungsfunktion, um Sequenzprobleme
						anzugehen, bei denen Zeit eine Variable ist."
						tag_list={['Google Spracherkennung', 'Neuronale Netze']}
						button_link="https://de.wikipedia.org/wiki/Long_short-term_memory"
					/>
				</li>

				<li>
					<HistoricalCard
						img_link="/facerecog.jpeg"
						img_alt="Gesichtserkennung"
						source_link="https://www.handelskraft.de/face-recognition-gruseltechnologie-oder-tor-zur-neuen-payment-welt/"
						source_text="Quelle: Handelskraft"
						heading="2006: Bessere Gesichtserkennungsalgorithmen"
						content="Gesichtserkennung ist eine Erkennungstechnik, die verwendet wird, um im Datensatz
						gespeicherte Gesichter zu erkennen. Es identifiziert ein Gesicht durch Vergleichen
						und Analysieren von Mustern basierend auf Gesichtskonturen durch trainierte
						neuronale Netzwerkmodelle. Im Jahr 2006 führte die Face Recognition Grand
						Challenge eine Bewertung der Gesichtserkennungsalgorithmen durch, und das Ergebnis
						der Bewertung ergab, dass die neuen Algorithmen zehnmal genauer waren als die
						Gesichtserkennungsalgorithmen von 2002 und 100-mal genauer als die von 1995.
						Einige der Algorithmen waren dazu in der Lage menschliche Teilnehmer bei der
						Erkennung von Gesichtern übertreffen und eineiige Zwillinge eindeutig
						identifizieren könnten."
						tag_list={['Gesichtserkennung', 'Neuronales Netzwerkmodell']}
						button_link="https://www.internetjustsociety.org/cosmonaut/facial-recognition-an-introduction"
					/>
				</li>

				<li>
					<HistoricalCard
						img_link="/mljetzt.jpg"
						img_alt="ML Jetzt vs Zukunft"
						source_link="https://www.informatec.com/en/machine-learning"
						source_text="Quelle: Informatec"
						heading="2006-20xx: ML Jetzt vs. Zukunft"
						content="Die Standford University definierte Machine Learning als „die Wissenschaft,
						Computer zum Handeln zu bringen, ohne explizit programmiert zu werden“. ML war der
						Schlüssel für einige der bedeutendsten technologischen Fortschritte. Es wird für
						die neue Industrie der selbstfahrenden Fahrzeuge, für die Erforschung der Galaxie
						und in Unternehmen eingesetzt. Einige häufige Aufgaben, die in der Geschäftswelt
						ML eingesetzt werden, sind: Verkaufsdatenanalyse, Produktempfehlungen, dynamische
						Preisgestaltung und mehr. Klar ist, dass ML auch in Zukunft im Mittelpunkt unseres
						Lebens stehen wird. Google arbeitet derzeit an einem Projekt zum maschinellen Lernen
						mit einem Ansatz namens Feinabstimmung von Anweisungen. Sie zielen darauf ab, ein ML-Modell
						zu trainieren, um Probleme bei der Verarbeitung natürlicher Sprache auf allgemeine
						Weise zu lösen."
						tag_list={['Geschäftswelt', 'Autonomes Fahren', 'Technologie']}
						button_link="http://mlclass.stanford.edu/#:~:text=Machine%20learning%20is%20the%20science,understanding%20of%20the%20human%20genome."
					/>
				</li>
			</ol>
		</div>
	</div>

	<div id="part-three" class="mt-32">
		<h1
			class="headline  text-2xl sm:text-3xl lg:text-4xl font-bold mb-12 ml-24 uppercase text-gray-100"
		>
			3. Arten von ML
		</h1>
		<div class="flex flex-col mt-8 mb-28 justify-center items-center text-center">
			<span class="text-2xl w-3/4 leading-relaxed mb-6 text-gray-300 text-center">
				Es gibt verschiedene Möglichkeiten, ML-Algorithmen zu trainieren, jede mit ihren eigenen
				Vor- und Nachteilen.
			</span>
		</div>

		<div class="flex flex-col w-[80%] sm:w-full ml-[10%] sm:ml-0 gap-y-60 items-center">
			<InformationTile title="Supervised Learning" class="mt-20">
				<div
					slot="content"
					class="text-gray-400 text-base sm:text-lg md:text-xl lg:text-2xl text-justify"
				>
					Beim Supervised Learning erhält der ML-Algorithmus einen kleinen und beschrifteten
					Trainingsdatensatz eines größeren Datensatzes, mit dem er arbeiten kann. Dies soll dem
					Algorithmus eine Grundidee des Problems, der Lösung und der zu behandelnden Datenpunkte
					geben. Der Algorithmus findet dann Beziehungen zwischen den gegebenen Parametern und hat
					eine Vorstellung davon, wie die Daten funktionieren und die Beziehung zwischen Eingabe und
					Ausgabe. Dann wird es auf dem endgültigen Datensatz eingesetzt, wo der Algorithmus mehr
					lernt und neue Muster und Beziehungen entdeckt, während er sich auf dem endgültigen
					Datensatz trainiert.
				</div>
				<div slot="right_slot">
					<AnimationContainer from_right>
						<img src="/supervised.jpg" alt="vikus_viewer" class="rounded-3xl shadow-2xl" />
					</AnimationContainer>
				</div>
			</InformationTile>
			<InformationTile title="Unsupervised Learning" right_side class="mt-20">
				<div
					slot="content"
					class="text-gray-400 text-base sm:text-lg md:text-xl lg:text-2xl text-justify"
				>
					Beim Unsupervised Learning muss der Datensatz nicht maschinenlesbar gemacht oder von
					Entwicklern gekennzeichnet werden, sodass das Programm viel größere Datensätze bearbeiten
					kann. Beim Unspervised Learning gibt es keine Gekennzeichnung, an denen das Programm
					abarbeiten, was zur Schaffung verborgener Strukturen führt. Die Erstellung dieser
					verborgenen Strukturen hilft dem unbeaufsichtigten Lernen, sich an die Daten anzupassen,
					indem verborgene Strukturen dynamisch geändert werden.
				</div>
				<div slot="right_slot">
					<AnimationContainer>
						<img src="/unsupervised.jpg" alt="vikus_viewer" class="rounded-3xl shadow-2xl" />
					</AnimationContainer>
				</div>
			</InformationTile>
			<InformationTile title="Reinforcement Learning" class="mt-20">
				<div
					slot="content"
					class="text-gray-400 text-base sm:text-lg md:text-xl lg:text-2xl text-justify"
				>
					Beim Reinforcement Learning handelt es sich um einen Algorithmus, der sich selbst
					verbessert und anhand einer Trial-and-Error-Methode aus neuen Situationen lernt. Es wird
					mit einem Interpreter und einem Belohnungssystem eingesetzt. Bei jeder Iteration des
					Algorithmus wird das Ausgabeergebnis an den Interpreter übergeben, der entscheidet, ob das
					Ergebnis gültig ist oder nicht. Falls das Programm die richtige Lösung findet, akzeptiert
					der Interpreter die Lösung, indem er dem Algorithmus eine Belohnung bereitstellt. Wenn das
					Ergebnis nicht gültig ist, muss der Algorithmus wiederholen, bis er ein besseres Ergebnis
					findet.
				</div>
				<div slot="right_slot">
					<AnimationContainer from_right>
						<img src="/reward.jpg" alt="vikus_viewer" class="rounded-3xl shadow-2xl" />
					</AnimationContainer>
				</div>
			</InformationTile>
		</div>

		<section class="mb-32 mx-6 mt-48 text-gray-100 text-center bg-gray-800 rounded-2xl p-6">
			<div class="flex justify-center">
				<div class="text-center w-3/4 ">
					<h2 class=" text-2xl sm:text-3xl lg:text-4xl font-bold mb-6 text-center">
						Übersicht der wichtigsten ML Begriffe
					</h2>
					<p class="text-2xl text-gray-400 mb-12">
						Hier wird auf einige wichtige Begriffe im Bereich ML eingegangen:
					</p>
				</div>
			</div>

			<div
				class="grid bg-gray-700 gap-12 rounded-2xl shadow-2xl p-6 grid-cols-1 sm:grid-cols-1 md:grid-cols-2 xl:grid-cols-4 lg:gap-x-12"
			>
				<OverviewSubCard
					icon="tablet"
					icon_size="24px"
					heading="Deep Learning"
					content="Deep Learning ist eine Anwendung von ML. Deep-Learning-Netzwerke interpretieren Big
					Data, sowohl unstrukturiert als auch strukturiert, und erkennen Muster in den Daten. Je
					mehr Daten sie trainieren und aus denen sie lernen können, desto fundierter und genauer
					werden ihre Entscheidungen sein. Ein reales Beispiel dafür wäre Chatbox, je mehr Daten
					es trainiert, desto besser funktioniert es."
				/>

				<OverviewSubCard
					icon="slack"
					icon_size="24px"
					heading="Neuronale Netzwerke"
					content="Neuronale Netze sind eng mit Deep Learning verwandt. Seine Aufgabe ist es, sequentielle
					Schichten von Neuronen zu erstellen, die das Verständnis der von einer Maschine
					gesammelten Daten vertiefen, um eine genaue Analyse zu ermöglichen. Ein neuronales
					Netzwerk besteht aus Schichten von Knoten, denen dann durch Koeffizienten eine
					Gewichtung zugewiesen, und das Netzwerk analysiert wird."
				/>

				<OverviewSubCard
					icon="user"
					icon_size="24px"
					heading="Regression"
					content="Regressionen in ML werden verwendet, um Beziehungen und Korrelationen zwischen
					verschiedenen Datentypen herzustellen. Regressionen können nützlich sein, wenn
					Ergebnisse basierend auf Daten in der Gegenwart vorhergesagt werden. Wenn sich
					beispielsweise ein Produkt bei einer bestimmten Personengruppe gut verkauft, kann das
					Geschäft in Gebieten, in denen diese Personen leben, mehr von diesem Produkt anbieten."
				/>

				<OverviewSubCard
					icon="users"
					icon_size="24px"
					heading="Clustering"
					content="Clustering, bei dem Datenpunkte nach Merkmalen und Attributen gruppiert werden, ist eine
					Form des unüberwachten Lernens. Clustering kann in mehreren Geschäftsbereichen verwendet
					werden, z. B. um Kundendemografie und Kaufverhalten in bestimmte Segmente für Targeting
					und Produktpositionierung zu organisieren."
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
					content="ML ermöglicht es uns, die riesigen Datenmengen des Internets zu erforschen und
					relevante Inhalte bereitzustellen."
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
					img_source="/Social_Media.jpg"
					img_alt="Social Media"
					heading="Social Media"
					content="Die Algorithmen hinter den Empfehlungssystemen von Social Media werden alle
					ML-basiert. Sie lernen von dem Nutzerverhalten und passen so den Feed an."
					read_more_link="https://webcare.plus/algorithmen-social-media/"
				/>

				<ApplicationCard
					img_source="/Personal_Content.jpg"
					img_alt="Persönliche Inhalte"
					heading="Persönliche Inhalte"
					content="Ob Werbungen oder vorgeschlagene Sucheinträge - ML Algorithmen analysieren das
					Nutzerverhalten im Internet und schlagen so personalisierte Inhalte vor."
					read_more_link="https://www.welt.de/wirtschaft/webwelt/article160308665/So-funktioniert-personalisierte-Werbung-im-Internet.html"
				/>

				<ApplicationCard
					img_source="/Chatbot.jpg"
					img_alt="Chatbot"
					heading="Chatbot"
					content="Besonders beim Kundenservice und -support setzen Unternehmen auf Chatbots, die die
					wichtigsten Informationen des Kundenproblems erfragen und analysieren."
					read_more_link="https://www.ibm.com/de-de/campaign/was-ist-ein-chatbot"
				/>

				<ApplicationCard
					img_source="/Content-Moderation.jpg"
					img_alt="Inhaltsverwaltung"
					heading="Inhaltsverwaltung"
					content="Die Inhaltsverwaltung in den sozialen Medien stellt die Anbieter vor große
					Herausforderungen. ML Algorithmen untersützen dabei, Hasskomentare o.Ä. zu
					identifizieren und zu löschen."
					read_more_link="https://de.wikipedia.org/wiki/Content-Moderation"
				/>

				<ApplicationCard
					img_source="/Gesichtserkennung.jpg"
					img_alt="Gesichtserkennung"
					heading="Gesichtserkennung"
					content="Sowohl in Smartphone-Kameras als auch in Überwachungskameras kommen ML Algorithmen zum
					Einsatz, um Gesichter und weitere Informationen zu erkennen."
					read_more_link="https://www.galileo.tv/technik/gesichtserkennung-wie-sie-funktioniert-und-warum-sie-gefaehrlich-werden-kann/"
				/>

				<ApplicationCard
					img_source="/Mobilität.jpg"
					img_alt="Mobilität"
					heading="Mobilität"
					content="Autonome Fahrzeuge sind nur die Spitze des Eisberges - ML Algorithmen unterstützt den
					Fahrer auch mit Einparkhilfen oder dem Halten der Fahrspur."
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
				<img src="/Hamid.jfif" class="rounded-full w-32 mb-4 mx-auto" alt="Avatar" />
				<h5 class="text-xl font-medium leading-tight mb-2">Hamid Omar</h5>
				<p class="text-gray-500 mb-2">Web designer</p>
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
