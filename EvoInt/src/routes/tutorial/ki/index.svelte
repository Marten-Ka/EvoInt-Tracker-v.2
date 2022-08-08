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
		{ text: '3. Arten von KI', href: '#part-three', icon: 'terminal' },
		{ text: '4. Anwendungsgebiete', href: '#part-four', icon: 'terminal' }
	];
</script>

<Header />

<div class="flex flex-col  text-center justify-center items-center mt-20">
	<h1
		class="headline text-sm  sm:text-lg md:text-xl lg:text-3xl xl:text-5xl 2xl:text-6xl font-bold uppercase text-gray-100 [text-shadow:0_4px_8px_rgba(255,255,255,0.25)]"
	>
		Künstliche Intelligenz
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
				img_link="/SebastianThrun.jpg"
				img_source="https://www.swisslife.com/content/internet/com/de/home/hub/interview-sebastian-thrun/_jcr_content/parsys/testimonial/image.1619729008567.transform/1_1_2480w/Sebastian_Thrun_Biobox.jpg"
				img_alt="Sebastian Thrun"
				quote="Niemand formuliert es so, aber für mich ist KI fast eine Geisteswissenschaft.
				Es ist wirklich der Versuch, menschliche Intelligenz und Kognition zu verstehen."
				quote_source="https://www.anacision.de/de/aktuelles/kuenstliche-intelligenz-definition"
				position="justify-start"
				author="Sebastian Thrun"
				sub_content="Ehemaliger Vizepräsident von Google"
			/>

			<QuoteCard
				img_link="/JohnMcCarthy.jpg"
				img_source="https://www.spiegel.de/netzwelt/web/john-mccarthy-der-vater-der-rechner-cloud-ist-tot-a-793795.html"
				img_alt="John McCarthy"
				quote="Es ist die Wissenschaft und Technik der Herstellung intelligenter Maschinen,
				insbesondere intelligenter Computerprogramme."
				quote_source="https://www.unaique.net/blog/definition-kuenstliche-intelligenz/"
				position="justify-end"
				author="John McCarthy"
				sub_content="US-amerikanischer Informatiker"
			/>

			<QuoteCard
				img_link="/EU.jpg"
				img_alt="EU"
				img_source="https://cdn.pixabay.com/photo/2014/01/27/18/13/europe-253311_1280.jpg"
				quote="Künstliche Intelligenz ist die Fähigkeit einer Maschine, menschliche Fähigkeiten
				wie logisches Denken, Lernen, Planen und Kreativität zu imitieren."
				quote_source="https://www.europarl.europa.eu/news/de/headlines/society/20200827STO85804/was-ist-kunstliche-intelligenz-und-wie-wird-sie-genutzt"
				position="justify-start"
				author="Europäisches Parlament"
			/>
		</section>

		<div class="flex flex-col justify-center items-center">
			<div class="flex flex-col mt-8 mb-28 justify-center items-center">
				<span
					class="text-base  sm:text-lg md:text-xl lg:text-2xl w-3/4 text-justify leading-relaxed mb-6 text-gray-300"
				>
					Tatsächlich ist der Begriff der Künstlichen Intelligenz (KI) bisher nicht eindeutig
					geklärt, weshalb es auch keine eindeutige Definition gibt. Das hängt sehr eng damit
					zusammen, dass der Begriff der menschlichen Intelligenz ebenfalls nicht exakt definiert
					ist. Jedoch tauchen im Zusammenhang mit KI immer wieder prägende Begriffe und Wörter auf,
					mit denen sich das Thema gut eingrenzen lässt. Diese Seite soll dazu dienen, einen
					Überblick rund um das Thema KI zu schaffen - von den Anfängen bis zur heutigen Zeit.
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
						img_link="/Turingmaschine.jpg"
						img_alt="Turingmaschine"
						source_link="https://anthrowiki.at/images/thumb/a/ad/Model_of_a_Turing_machine.jpg/375px-Model_of_a_Turing_machine.jpg"
						source_text="Quelle: Anthrowiki"
						heading="1936: Turingmaschine"
						content="Alan Turing, ein britischer Mathematiker, legte 1936 schon den Grundstein für das,
						was wir heute unter Künstlicher Intelligenz verstehen. Mit seinen Theorien konnte
						er beweisen, dass eine Rechenmaschine (auch bezeichnet als 'Turingmaschine') in
						der Lage wäre, kognitive Prozesse auszuführen, sofern sich diese in mehrere kleine
						Schritte zerlegen und algorithmisch darstellen lassen."
						tag_list={['Alan Turing', 'Grundstein der KI']}
						button_link="https://de.wikipedia.org/wiki/Turingmaschine"
					/>
				</li>

				<li>
					<HistoricalCard
						img_link="/DartmouthConference.jpg"
						img_alt="Dartmouth Conference"
						source_link="https://cyfuture.com/blog/wp-content/uploads/2020/04/Dartmouth-Conference-in-1956.jpg"
						source_text="Quelle: Cyfuture"
						heading="1956: Der Begriff KI entsteht"
						content="1956 treffen sich Wissenschaftler zu einer Konferenz am Dartmouth College im
						US-Bundesstaat New Hampshire und debattieren über die Simulation von menschlicher
						Intelligenz durch Maschinen. John McCartney schlägt dafür den Begriff 'Künstliche
						Intelligenz' vor. Während der Konferenz entsteht außerdem das erste KI-Programm
						der Welt - der 'Logic Theorist', der es schafft, mehrere mathematische Lehrsätze
						zu beweisen."
						tag_list={['Dartmouth Konferenz', 'John McCarthy']}
						button_link="https://de.wikipedia.org/wiki/Dartmouth_Conference"
					/>
				</li>

				<li>
					<HistoricalCard
						img_link="/ELIZA.jpg"
						img_alt="ELIZA"
						source_link="https://moodswag.com/wp-content/uploads/2020/09/Eliza.jpg"
						source_text="Quelle: Moodswag"
						heading="1966: Der erste Chatbot"
						content="1966 entwickelt der deutsch-amerikanische Informatiker Joseph Weizenbaum vom
						Massachusetts Institute of Technology das Computerprogramm 'ELIZA', welches mit
						Menschen kommunizieren kann. ELIZA kann mehrere Gesprächspartner simulieren, wie
						beispielsweise einen Psychotherapeuten. Jedoch sind die genutzten Mittel zur
						Simulation des Gesprächs noch recht rudimentär geskriptet"
						tag_list={['Joseph Weizenbaum', 'ELIZA']}
						button_link="https://de.wikipedia.org/wiki/ELIZA"
					/>
				</li>

				<li>
					<HistoricalCard
						img_link="/MYCIN.jpg"
						img_alt="MYCIN"
						source_link="https://www.bibliomedmanager.de/fileadmin/user_upload/alle-Portale/Bilder/TANGO/sp/2018/04/gettyimages_894319072.jpg"
						source_text="Quelle: Bibliomedmanager"
						heading="1972: KI gelangt in die Medizin"
						content="Die KI ist für viele schon lange kein Fremdwort mehr, doch jetzt findet sie ihren
						ersten Einsatz in der realen Welt. Das von Ted Shortlife an der Stanford
						University entwickelte Expertensystem 'MYCIN' wird zur Diagnose und Therapie von
						Infektionskrankheiten eingesetzt. Doch auch wenn das System hohe Trefferquoten
						erzielt, erlangte es nicht die Bedeutung in der Medizin, die man sich erhofft
						hatte. Die Bereitschaft gegenüber solchen Systemen war schlicht zu gering, als
						dass sich Ärzte auf dessen Diagnose verlassen wollten."
						tag_list={['MYCIN', 'Medizin']}
						button_link="https://de.wikipedia.org/wiki/Mycin_(Expertensystem)"
					/>
				</li>

				<li>
					<HistoricalCard
						img_link="/NETTalk.jpg"
						img_alt="NETtalk"
						source_link="https://fscl01.fonpit.de/userfiles/7611461/image/AI-artificial-intelligence-robot/AI-robot_12-w810h462.jpg"
						source_text="Quelle: Fonpit"
						heading="1986: Computer lernt sprechen"
						content="Terrence J. Sejnowski und Charles Rosenberg bringen ihrem Programm 'NETtalk'
						mithilfe von Beispielsätzen und Phonemketten das Sprechen bei. 'NETtalk' kann
						Wörter lesen und korrekt aussprechen sowie das Gelernte auf ihm unbekannte Wörter
						anwenden. Aufgrund dieser Fähigkeit, die darauf beruht, dass das Programm mit
						großen Datenmengen befüllt wird und daraus eigene Schlüsse zieht, gehört es
						ebenfalls zu den frühen künstlichen neuronalen Netzen."
						tag_list={['NETtalk', 'Neuronale Netze']}
						button_link="https://de.wikipedia.org/wiki/NETtalk"
					/>
				</li>

				<li>
					<HistoricalCard
						img_link="/DeepBlue.jpg"
						img_alt="Deep Blue"
						source_link="https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg"
						source_text="Quelle: Wikimedia"
						heading="1997: KI schlägt Schachweltmeister"
						content="Die KI 'Deep Blue' der Firma IBM, welche für das Schach spielen konzipiert ist,
						bezwingt 1997 den amtierenden Weltmeister Garry Kasparov. Damit ist der bisher von
						Menschen dominierte Bereich des Schachs von einer KI übernommen worden. Dieser
						historische Erfolg wird nur leicht von Kritikern getrübt, die einwerfen, dass
						'Deep Blue' nicht durch kognitive Intelligenz, sondern durch das Berechnen aller
						möglichen Züge gewonnen habe."
						tag_list={['Deep Blue', 'KI im Schach']}
						button_link="https://de.wikipedia.org/wiki/Long_short-term_memory"
					/>
				</li>

				<li>
					<HistoricalCard
						img_link="/IBM_KI.jpg"
						img_alt="IBM"
						source_link="https://www.tanikal.com/wp-content/uploads/2016/12/IBM-Logo-Wallpaper-HD.jpg"
						source_text="Quelle: Tanikal"
						heading="2011: 'Watson' gewinnt Quizshow"
						content="Das Computerprogramm 'Watson' tritt 2011 in einer US-amerikanischen TV-Quizshow
						gegen menschliche Mitspieler an und gewinnt die Show. Damit beweist die KI, dass
						sie tatsächlich die natürliche Sprache versteht und eine schnellere
						Reaktionsgeschwindigkeit als die Mitspieler hat."
						tag_list={['Watson', 'IBM']}
						button_link="https://de.wikipedia.org/wiki/Watson_(K%C3%BCnstliche_Intelligenz)"
					/>
				</li>

				<li>
					<HistoricalCard
						img_link="/KI_im_Alltag.jpeg"
						img_alt="KI im Alltag"
						source_link="https://medsolut.com/wp-content/uploads/2021/05/20210506_MedSolut_AI_Daily-Life_Blog-Article.jpeg"
						source_text="Quelle: Medsolut"
						heading="2011-Heute: KI erreicht den Alltag"
						content="In den letzten zehn Jahren haben die Wissenschaft und die Technikbranche enorme
						Fortschritte im Bereich der KI gemacht. Diese bahnbrechenden Entwicklungen haben
						der KI den Weg in den Alltag gebahnt: ob bei Google, in den sozialen Medien, Siri,
						Cortana oder Alexa - überall tritt sie auf. Gesamte Unternehmen und private
						Haushalte sind mittlerweile über KI-gesteuerte Systeme vernetzt und kommunizieren
						miteinander, ohne dass die Endverbraucher davon etwas mitbekommen."
						tag_list={['KI im Alltag', 'Sprachassistenten']}
						button_link="https://mixed.de/ki-im-alltag/"
					/>
				</li>

				<li>
					<HistoricalCard
						img_link="/KI_der_Zukunft.jpg"
						img_alt="KI der Zukunft"
						source_link="https://www.verlagederzukunft.de/wp-content/uploads/2018/12/KI_Algemein_VdZ.jpg"
						source_text="Quelle: Verlage der Zukunft"
						heading="20xx: Die KI der Zukunft"
						content="Trotz der bahnbrechenden Entwicklung des vergangenen Jahrzehnts steckt die
						Forschung der KI noch in ihren Anfängen. Das Ziel der Zukunft wird es sein, KI
						zuverlässiger und sicherer in Bereichen wie dem autonomen Fahren, der Raumfahrt
						und besonders in der Medizin zu gestalten. Bisher ist es außerdem nicht gelungen,
						eine sogenannte 'starke KI' zu schaffen, die ihr Wissen auf sehr viele Bereiche
						übertragen und somit uns Menschen in jeder Hinsicht übertrumpfen kann. All das
						birgt auch Gefahren, weshalb ethische Fragen zur Forschung und Entwicklung der KI
						immer mehr in der Vordergrund rücken. Die primäre Frage ist und bleibt dabei 'KI -
						Fluch oder Segen für den Menschen?'"
						tag_list={['Starke KI', 'Ethik & Moral']}
						button_link="https://mixed.de/ki-im-alltag/"
					/>
				</li>
			</ol>
		</div>
	</div>

	<div id="part-three" class="mt-32">
		<h1
			class="headline  text-2xl sm:text-3xl lg:text-4xl font-bold mb-12 ml-24 uppercase text-gray-100"
		>
			3. Arten von KI
		</h1>

		<div class="flex flex-col w-[80%] sm:w-full ml-[10%] sm:ml-0 gap-y-60 items-center ">
			<InformationTile title="Schwache KI" class="mt-20">
				<div
					slot="content"
					class="text-gray-400 text-base sm:text-lg md:text-xl lg:text-2xl text-justify"
				>
					Ein KI-System, das nur für die Ausführung einer bestimmten Aufgabe entwickelt und
					trainiert wurde. Es benötigt meist zusätzliche menschliche Intervention und kann ihr
					Wissen nicht auf andere Bereiche ausweiten. Beispiele aus dem Alltag sind
					Sprachassistenten wie Siri und Alexa oder Industrieroboter.
				</div>
				<div slot="right_slot">
					<AnimationContainer from_right>
						<img src="/siri.jpg" alt="vikus_viewer" class="rounded-3xl shadow-2xl" />
					</AnimationContainer>
				</div>
			</InformationTile>
			<InformationTile title="Starke KI" right_side class="mt-20">
				<div
					slot="content"
					class="text-gray-400 text-base sm:text-lg md:text-xl lg:text-2xl text-justify"
				>
					Auch bekannt als allgemeine künstliche Intelligenz kann die starke KI die kognitiven
					Fähigkeiten des menschlichen Gehirns nachbilden. Somit kann sie auch unbekannte Aufgaben
					lösen, indem sie Wissen aus anderen Bereichen anwendet und selbstständig eine Lösung
					findet. Diese Art von KI ist jedoch nur ein theoretisches Modell, welches es so bisher
					nicht gibt.
				</div>
				<div slot="right_slot">
					<AnimationContainer>
						<img src="/Starke_KI.jpg" alt="vikus_viewer" class="rounded-3xl shadow-2xl" />
					</AnimationContainer>
				</div>
			</InformationTile>
		</div>

		<section class="mb-32 mx-6 mt-48 text-gray-100 text-center bg-gray-800 rounded-2xl p-6">
			<div class="flex justify-center">
				<div class="text-center w-3/4 ">
					<h2 class=" text-2xl sm:text-3xl lg:text-4xl font-bold mb-6 text-center">
						4 Typen von KI
					</h2>
					<p class="text-2xl text-gray-400 mb-12">
						In <a
							class="text-blue-500 underline"
							href="https://www.govtech.com/computing/understanding-the-four-types-of-artificial-intelligence.html"
						>
							diesem Artikel</a
						>
						erklärte Arend Hintze, ein Assistenzprofessor für integrative Biologie, Computerwissenschaft
						und Ingenieurwesen an der Michigan State University, dass KI in vier Arten unterteilt werden
						kann. Die vier Kategorien sind:
					</p>
				</div>
			</div>

			<div
				class="grid bg-gray-700 gap-12 rounded-2xl shadow-2xl p-6 grid-cols-1 sm:grid-cols-1 md:grid-cols-2 xl:grid-cols-4 lg:gap-x-12"
			>
				<OverviewSubCard
					icon="tablet"
					icon_size="24px"
					heading="1. Reaktive Maschinen (reactive machines)"
					content="Diese KI-Systeme besitzen keinen eigenen Speicher, aus dem sie Erfahrungen schöpfen
					können, womit sie auch nur einem bestimmten Zweck dienen und aufgabenspezifisch sind.
					Ein Beispiel dafür ist das vorhin aufgeführte, von IBM entwickelte Schachprogramm Deep
					Blue. Dieses System kann Figuren auf dem Schachbrett erkennen und Vorhersagen treffen,
					jedoch aber nicht aus früheren Erkenntnissen lernen."
				/>

				<OverviewSubCard
					icon="slack"
					icon_size="24px"
					heading="2. Begrenzte Speicherkapazität (limited memory)"
					content="Anders als die reaktiven Maschinen verfügen diese KI-Systeme über einen Speicher ('ein
					Gedächtnis'), mit welchem sie auf frühere Erfahrungen zurückgreifen und somit neue
					Kenntnisse ziehen können. Solche Systeme kommen unter anderem in autonomen Fahrzeugen
					zum Einsatz."
				/>

				<OverviewSubCard
					icon="user"
					icon_size="24px"
					heading="3. Theorie des Geistes (theory of mind)"
					content="Dieser Typ ähnelt immer mehr einer starken KI, denn solche KIs verfügen über
					soziale Intelligenz und können somit Emotionen verstehen. Diese Art von KI wird in der
					Lage sein, menschliche Absichten zu erkennen und Verhalten vorherzusagen, was es ihr
					leichter machen wird, Bestandteil menschlicher Teams zu werden."
				/>

				<OverviewSubCard
					icon="users"
					icon_size="24px"
					heading="Selbstwahrnehmung"
					content="Künstliche Intelligenzen von diesem Typ besitzen mindestens eine Intelligenz auf
					menschlichem Niveau und einen Sinn für sich selbst, was Ihnen ein eigenes Bewusstsein
					gibt. Sie verstehen ihren eigenen aktuellen Zustand und können uns Menschen in vielen
					Dingen übertreffen, was auch Gefahren birgt."
				/>
			</div>
		</section>
	</div>

	<div id="part-four" class="grid mt-32">
		<h1
			class="headline text-2xl sm:text-3xl lg:text-4xl font-bold mb-12 ml-24 uppercase text-gray-100"
		>
			4. Anwendungsgebiete
		</h1>

		<div class="grid justify-center items-center justify-self-center w-3/4">
			<div
				class="grid gap-12 m-6 grid-cols-1 md:grid-cols-2 lg:grid-cols-2 xl:grid-cols-2 2xl:grid-cols-4"
			>
				<ApplicationCard
					img_source="/Robotik.jpg"
					img_alt="Robotik"
					heading="Robotik"
					content="Besonders in der Industrie sind KI-gesteuerte Roboter weit verbreitet - hier
					übernehmen sie beispielsweise einen Großteil der Fertigung in der Autobranche."
					read_more_link="https://www.infineon.com/cms/de/discoveries/grundlagen-robotics/"
				/>

				<ApplicationCard
					img_source="/Suchmaschine.jpg"
					img_alt="Suchmaschine"
					heading="Suchmaschine"
					content="KI ermöglicht es uns, die riesigen Datenmengen des Internets zu erforschen und
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
					img_source="/Spam_Filter.jpg"
					img_alt="Spam Filter"
					heading="Spam Filter"
					content="Der größte Teil aller Spam-Mails wird schon von KI basierten Filtern der Mail-Anbieter
					gelöscht, bevor sie überhaupt in das Postfach gelangen."
					read_more_link="https://de.wikipedia.org/wiki/Spamfilter"
				/>

				<ApplicationCard
					img_source="/Social_Media.jpg"
					img_alt="Social Media"
					heading="Social Media"
					content="Die Algorithmen hinter den Empfehlungssystemen von Social Media sind alle KI-basiert.
					Sie lernen von dem Nutzerverhalten und passen so den Feed an."
					read_more_link="https://webcare.plus/algorithmen-social-media/"
				/>

				<ApplicationCard
					img_source="/Personal_Content.jpg"
					img_alt="Personal Content"
					heading="Personal Content"
					content="Ob Werbungen oder vorgeschlagene Sucheinträge - KIs analysieren das Nutzerverhalten im
					Internet und schlagen so personalisierte Inhalte vor."
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
					Herausforderungen. KIs untersützen dabei, Hasskomentare o.Ä. zu identifizieren und zu
					löschen."
					read_more_link="https://de.wikipedia.org/wiki/Content-Moderation"
				/>

				<ApplicationCard
					img_source="/Gesichtserkennung.jpg"
					img_alt="Gesichtserkennung"
					heading="Gesichtserkennung"
					content="Sowohl in Smartphone-Kameras als auch in Überwachungskameras kommen KIs zum Einsatz,
					um Gesichter und weitere Informationen zu erkennen."
					read_more_link="https://www.galileo.tv/technik/gesichtserkennung-wie-sie-funktioniert-und-warum-sie-gefaehrlich-werden-kann/"
				/>

				<ApplicationCard
					img_source="/Mobilität.jpg"
					img_alt="Mobilität"
					heading="Mobilität"
					content="Autonome Fahrzeuge sind nur die Spitze des Eisberges - KI unterstützt den Fahrer auch
					mit Einparkhilfen oder dem Halten der Fahrspur."
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
				<p class="text-gray-500 mb-2">Web designer</p>
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
		</div>
	</div>
</div>

<Footer />

<style lang="postcss">
</style>
