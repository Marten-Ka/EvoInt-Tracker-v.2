<script lang="ts">
	import TutorialRedirectButton from '../../../components/_TutorialRedirectButton.svelte';
	import AnimationContainer from '../../../components/AnimationContainer.svelte';
	import Footer from '../../../components/Footer.svelte';
	import Header from '../../../components/Header.svelte';
	import InformationTile from '../../../components/InformationTile.svelte';
	import Icon from '../../../components/Icon.svelte';

	const redirects = [
		{ text: '1. Der Begriff der Machine Learning', href: '#part-one', icon: 'terminal' },
		{ text: '2. Die historische Entwicklung von ML', href: '#part-two', icon: 'terminal' },
		{ text: '3. Die Arten von ML', href: '#part-three', icon: 'terminal' },
		{ text: '4. Übersicht der wichtigsten Begriffe', href: '#part-three', icon: 'terminal' },
    { text: '5. Anwendungsgebiete von ML', href: '#part-five', icon: 'terminal' },
	];
</script>
<Header />

<div class="flex flex-col text-center justify-center items-center mt-20">
	<h1
		class="headline text-7xl font-bold uppercase text-gray-100 [text-shadow:0_4px_8px_rgba(255,255,255,0.25)]"
	>
		Machine Learning
	</h1>
	<h2 class="mt-2 mb-32 text-3xl font-semibold text-gray-400 uppercase">
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

<div class="flex flex-col  mt-32">
	<div id="part-one" class="mt-32">
		<h1 class="headline text-4xl font-bold mb-12 ml-24 uppercase text-gray-100">
			1. Der Begriff der Machine Learning
		</h1>

		<section
			class="flex flex-col place-content-start gap-16 mx-6 my-16 p-16 text-center md:text-left shadow-lg rounded-md bg-cover"
			style="background-image: url(https://mdbcdn.b-cdn.net/img/Photos/Others/background2.jpg)"
		>
			<div class="flex justify-start">
				<div class="max-w-4xl xl:max-w-6xl 2xl:max-w-7xl">
					<div class="block p-6 rounded-lg shadow-lg bg-white m-4">
						<div class="md:flex md:flex-row">
							<div
								class="md:w-96 w-36 flex justify-center items-center mb-6 lg:mb-0 mx-auto md:mx-0"
							>
								<img
									src="https://www.ibm.com/design/language/877b208e9d05b37650a70e55867861bd/core_gray60_on_white.svg"
									class="rounded-full shadow-md"
									alt="IBM Cloud Education"
								/>
							</div>
							<div class="md:ml-6 place-self-center">
								<p class="text-gray-500 text-xl font-semibold italic mb-6">
									"Maschinelles Lernen, Machine Learning (ML), ist ein Zweig der künstlichen Intelligenz (KI) und Computerwissenschaft, 
                  der sich auf die Verwendung von Daten und Algorithmen konzentriert, 
                  um die Art und Weise, wie Menschen lernen, zu imitieren und die Genauigkeit schrittweise zu verbessern."
								</p>
								<p class="font-semibold text-xl mb-2 text-gray-800">IBM Cloud Education</p>
							</div>
						</div>
					</div>
				</div>
			</div>

			<div class="flex justify-end">
				<div class="max-w-4xl xl:max-w-6xl 2xl:max-w-7xl">
					<div class="block p-6 rounded-lg shadow-lg bg-white m-4">
						<div class="md:flex md:flex-row">
							<div
								class="md:w-96 w-36 flex justify-center items-center mb-6 lg:mb-0 mx-auto md:mx-0"
							>
								<img
									src="https://www.andrewng.org/static/c5eb39b8da664718384eefcbc915f5cd/25582/andrew-ng-homepage.webp"
									class="rounded-full shadow-md"
									alt="Andrew Ng"
								/>
							</div>
							<div class="md:ml-6 place-self-center">
								<p class="text-gray-500 text-xl font-semibold italic mb-6">
									"Maschinelles Lernen ist die Wissenschaft, Computer zum Handeln zu bringen, ohne explizit programmiert zu werden"
								</p>
								<p class="font-semibold text-xl mb-2 text-gray-800">Andrew Ng</p>
								<p class="font-semibold text-gray-500 mb-0">Direktor des Labors für künstliche Intelligenz in Stanford</p>
							</div>
						</div>
					</div>
				</div>
			</div>

			<div class="flex justify-start">
				<div class="max-w-4xl xl:max-w-6xl 2xl:max-w-7xl">
					<div class="block p-6 rounded-lg shadow-lg bg-white m-4">
						<div class="md:flex md:flex-row">
							<div
								class="md:w-96 w-36 flex justify-center items-center mb-6 lg:mb-0 mx-auto md:mx-0"
							>
								<img
									src="https://www.cs.ox.ac.uk/files/8605//PTAIT_20161031_0020%20%282%29.jpg"
									class="rounded-full shadow-md"
									alt="Michael Wooldridge"
								/>
							</div>
							<div class="md:ml-6 place-self-center">
								<p class="text-gray-500 text-xl font-semibold italic mb-6">
									"Maschinelles Lernen zielt darauf ab, Computer zu bauen, die lernen können, Entscheidungen zu treffen oder Aufgaben auszuführen, 
                  ohne dass ihnen explizit gesagt wird, wie sie das tun sollen"
								</p>
								<p class="font-semibold text-xl mb-2 text-gray-800">Michael Wooldridge</p>
								<p class="font-semibold text-gray-500 mb-0">Professor für Informatik an der Universität Oxford</p>
							</div>
						</div>
					</div>
				</div>
			</div>
		</section>

		<div class="flex flex-col justify-center items-center text-center">
			<div class="flex flex-col mt-8 mb-28 justify-center items-center text-center">
				<span class="text-2xl w-3/4 text-justify leading-relaxed mb-6 text-gray-300">
					Machine Learning, auf Deutsch: Machinelles Lernen, ist heute für viele Organisationen ein notwendiger Aspekt der modernen Geschäftswelt und Forschung. 
          Es verwendet Algorithmen und neuronale Netzwerkmodelle, um Computersysteme bei der schrittweisen Verbesserung ihrer Leistung zu unterstützen. 
          Diese Seite soll dazu dienen, einen Überblick rund um das Thema ML zu schaffen - von den Anfängen bis zur heutigen Zeit.
				</span>
			</div>
		</div>
	</div>

	<div id="part-two" class="mt-32">
		<h1 class="headline text-4xl font-bold mb-12 ml-24 uppercase text-gray-100">
			2. Die historische Entwicklung von ML
		</h1>

		<div class="flex flex-col items-center">
			<ol class="border-l-2 border-blue-600">
				<li>
					<div class="md:flex flex-start">
						<div class="bg-blue-600 w-6 h-6 flex items-center justify-center rounded-full -ml-3">
							<svg
								aria-hidden="true"
								focusable="false"
								data-prefix="fas"
								class="text-white w-3 h-3"
								role="img"
								xmlns="http://www.w3.org/2000/svg"
								viewBox="0 0 448 512"
							>
								<path
									fill="currentColor"
									d="M0 464c0 26.5 21.5 48 48 48h352c26.5 0 48-21.5 48-48V192H0v272zm64-192c0-8.8 7.2-16 16-16h288c8.8 0 16 7.2 16 16v64c0 8.8-7.2 16-16 16H80c-8.8 0-16-7.2-16-16v-64zM400 64h-48V16c0-8.8-7.2-16-16-16h-32c-8.8 0-16 7.2-16 16v48H160V16c0-8.8-7.2-16-16-16h-32c-8.8 0-16 7.2-16 16v48H48C21.5 64 0 85.5 0 112v48h448v-48c0-26.5-21.5-48-48-48z"
								/>
							</svg>
						</div>
						<div class="max-w-md rounded overflow-hidden shadow-lg ml-6 mb-6">
              <div class="relative group">
                <img
                  class="w-full block h-auto"
                  src="../../../static/samuel.jpeg"
                  alt="Turingmaschine"
                />
                <a href="https://medium.com/ibm-data-ai/the-first-of-its-kind-ai-model-samuels-checkers-playing-program-1b712fa4ab96" target="_blank" class="opacity-0 bottom-0 absolute text-left group-hover:opacity-80 w-full border-[0.5px] rounded-t bg-gray-200 text-gray-700 px-6 py-1 ">
                  Quelle: Micro Medium
                </a>
              </div>
							<div class="px-6 py-4 bg-gray-100">
								<div class="font-bold text-2xl mb-2">1952: Samuel's Checker Player</div>
								<p class="text-gray-700 text-base">
									Arthur Samuel von IBM entwickelte 1952 ein Computerprogramm zum Damespiel für den IBM 701. Sein Entwurf beinhaltete eine Punktefunktion, 
                  die die Positionen der Figuren auf dem Brett nutzte. Die Bewertungsfunktion versuchte, die Gewinnchancen jeder Seite zu messen.
                  Samuel entwarf auch eine Reihe von Mechanismen, die es ihm ermöglichten, sein Programm zu verbessern. Bei dem, was Samuel Auswendiglernen nannte, 
                  erinnerte sich sein Programm an alle Positionen, die es bereits gesehen hatte, und kombinierte dies mit den Werten der Belohnungsfunktion. 
                  1952 prägte Arthur Samuel erstmals den Begriff „Machine Learning“.
								</p>
							</div>
							<div class="flex flex-col gap-4 px-6 pt-4 pb-4 bg-gray-100">
								<div>
									<span
										class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
									>
										Arthur Samuel
									</span>
									<span
										class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
									>
										Grundstein der ML
									</span>
								</div>
								<div>
									<form action="https://webdocs.cs.ualberta.ca/~jonathan/publications/ai_publications/samuel.pdf">
										<button
											type="submit"
											class="inline-block px-4 py-1.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
											data-mdb-ripple="true"
										>
											Read more
										</button>
									</form>
								</div>
							</div>
						</div>
					</div>
				</li>

				<li>
					<div class="md:flex flex-start">
						<div class="bg-blue-600 w-6 h-6 flex items-center justify-center rounded-full -ml-3">
							<svg
								aria-hidden="true"
								focusable="false"
								data-prefix="fas"
								class="text-white w-3 h-3"
								role="img"
								xmlns="http://www.w3.org/2000/svg"
								viewBox="0 0 448 512"
							>
								<path
									fill="currentColor"
									d="M0 464c0 26.5 21.5 48 48 48h352c26.5 0 48-21.5 48-48V192H0v272zm64-192c0-8.8 7.2-16 16-16h288c8.8 0 16 7.2 16 16v64c0 8.8-7.2 16-16 16H80c-8.8 0-16-7.2-16-16v-64zM400 64h-48V16c0-8.8-7.2-16-16-16h-32c-8.8 0-16 7.2-16 16v48H160V16c0-8.8-7.2-16-16-16h-32c-8.8 0-16 7.2-16 16v48H48C21.5 64 0 85.5 0 112v48h448v-48c0-26.5-21.5-48-48-48z"
								/>
							</svg>
						</div>
						<div class="max-w-md rounded overflow-hidden shadow-lg ml-6 mb-6">
              <div class="relative group">
                <img
                  class="w-full block h-auto"
                  src="../../../perceptron.gif"
                  alt="Perzeptron "
                />
                <a href="https://medium.com/towards-data-science/what-the-hell-is-perceptron-626217814f53" target="_blank" class="opacity-0 bottom-0 absolute text-left group-hover:opacity-80 w-full border-[0.5px] rounded-t bg-gray-200 text-gray-700 px-6 py-1">
                  Quelle: Medium
                </a>
              </div>
							<div class="px-6 py-4 bg-gray-100">
								<div class="font-bold text-2xl mb-2">1957: Der Perzeptron</div>
								<p class="text-gray-700 text-base">
									1957 schuf Frank Rosenblatt Perzeptron, indem er Donald Hebbs Modell der Gehirnzellinteraktion mit Arthur Samuels 
                  Bemühungen um Machine Learining kombinierte. Das Perzeptron war ursprünglich als Maschine geplant, nicht als Programm.
                  Die Software wurde ursprünglich für den IBM 704 entwickelt und in einer speziell angefertigten Maschine namens Mark 1 Perceptron 
                  installiert, die für die Bilderkennung konstruiert worden war. Dadurch wurden die Software und die Algorithmen übertragbar und für 
                  andere Maschinen verfügbar.
                  Obwohl das Perzeptron vielversprechend schien, konnte es viele Arten von visuellen Mustern nicht erkennen, was zu Frustration führte 
                  und die Erforschung neuronaler Netzwerke blockierte. Es hat bei den Investoren zu Frustration geführt und Finanzierungen wurden zurückgenommen.
								</p>
							</div>
							<div class="flex flex-col gap-4 px-6 pt-4 pb-4 bg-gray-100">
								<div>
									<span
										class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
									>
										Bilderkennung
									</span>
									<span
										class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
									>
                    Frank Rosenblatt
									</span>
								</div>
								<div>
									<form action="https://de.wikipedia.org/wiki/Perzeptron">
										<button
											type="submit"
											class="inline-block px-4 py-1.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
											data-mdb-ripple="true"
										>
											Read more
										</button>
									</form>
								</div>
							</div>
						</div>
					</div>
				</li>
				<li>
					<div class="md:flex flex-start">
						<div class="bg-blue-600 w-6 h-6 flex items-center justify-center rounded-full -ml-3">
							<svg
								aria-hidden="true"
								focusable="false"
								data-prefix="fas"
								class="text-white w-3 h-3"
								role="img"
								xmlns="http://www.w3.org/2000/svg"
								viewBox="0 0 448 512"
							>
								<path
									fill="currentColor"
									d="M0 464c0 26.5 21.5 48 48 48h352c26.5 0 48-21.5 48-48V192H0v272zm64-192c0-8.8 7.2-16 16-16h288c8.8 0 16 7.2 16 16v64c0 8.8-7.2 16-16 16H80c-8.8 0-16-7.2-16-16v-64zM400 64h-48V16c0-8.8-7.2-16-16-16h-32c-8.8 0-16 7.2-16 16v48H160V16c0-8.8-7.2-16-16-16h-32c-8.8 0-16 7.2-16 16v48H48C21.5 64 0 85.5 0 112v48h448v-48c0-26.5-21.5-48-48-48z"
								/>
							</svg>
						</div>
						<div class="max-w-md rounded overflow-hidden shadow-lg ml-6 mb-6">
              <div class="relative group">
                <img
                  class="w-full block h-auto"
                  src="../../../static/neighbor.png"
                  alt="Der Nearest-Neighbor-Algorithmus"
                />
                <a href="https://towardsdatascience.com/similarity-search-with-ivfpq-9c6348fd4db3" target="_blank" class="opacity-0 bottom-0 absolute text-left group-hover:opacity-80 w-full border-[0.5px] rounded-t bg-gray-200 text-gray-700 px-6 py-1">
                  Quelle: Towards Data Science
                </a>
              </div>
							<div class="px-6 py-4 bg-gray-100">
								<div class="font-bold text-2xl mb-2">1967: Der Nearest Neighbor Algorithmus </div>
								<p class="text-gray-700 text-base">
									1967 wurde der Beginn der grundlegenden Mustererkennung durch die Konzeption des Nearest-Neighbor-Algorithmus erreicht. 
                  Marcello Pelillo ist berühmt geworden, weil er die „Nearest-Neighbor-Regel“ erfunden hat. Dieser Algorithmus wurde zur 
                  Kartierung von Routen verwendet und war einer der frühesten Algorithmen, die verwendet wurden, um eine Lösung für das 
                  Problem des Handlungsreisenden zu finden, die effizienteste Route zu finden. Unter Verwendung dieser gibt ein Verkäufer 
                  eine ausgewählte Stadt ein und lässt das Programm wiederholt die nächstgelegenen Städte besuchen, bis alle besucht wurden.
								</p>
							</div>
							<div class="flex flex-col gap-4 px-6 pt-4 pb-4 bg-gray-100">
								<div>
									<span
										class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
									>
                    Marcello Pelillo
									</span>
									<span
										class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
									>
										Der Nearest-Neighbor-Algorithmus
									</span>
								</div>
								<div>
									<form action="https://de.wikipedia.org/wiki/Nearest-Neighbor-Heuristik">
										<button
											type="submit"
											class="inline-block px-4 py-1.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
											data-mdb-ripple="true"
										>
											Read more
										</button>
									</form>
								</div>
							</div>
						</div>
					</div>
				</li>
				<li>
					<div class="md:flex flex-start">
						<div class="bg-blue-600 w-6 h-6 flex items-center justify-center rounded-full -ml-3">
							<svg
								aria-hidden="true"
								focusable="false"
								data-prefix="fas"
								class="text-white w-3 h-3"
								role="img"
								xmlns="http://www.w3.org/2000/svg"
								viewBox="0 0 448 512"
							>
								<path
									fill="currentColor"
									d="M0 464c0 26.5 21.5 48 48 48h352c26.5 0 48-21.5 48-48V192H0v272zm64-192c0-8.8 7.2-16 16-16h288c8.8 0 16 7.2 16 16v64c0 8.8-7.2 16-16 16H80c-8.8 0-16-7.2-16-16v-64zM400 64h-48V16c0-8.8-7.2-16-16-16h-32c-8.8 0-16 7.2-16 16v48H160V16c0-8.8-7.2-16-16-16h-32c-8.8 0-16 7.2-16 16v48H48C21.5 64 0 85.5 0 112v48h448v-48c0-26.5-21.5-48-48-48z"
								/>
							</svg>
						</div>
						<div class="max-w-md rounded overflow-hidden shadow-lg ml-6 mb-6">
              <div class="relative group">
                <img
                  class="w-full block h-auto"
                  src="../../../static/aiki.png"
                  alt="AI vs ML"
                />
                <a href="https://towardsai.net/p/machine-learning/differences-between-ai-and-machine-learning-1255b182fc6" target="_blank" class="opacity-0 bottom-0 absolute text-left group-hover:opacity-80 w-full border-[0.5px] rounded-t bg-gray-200 text-gray-700 px-6 py-1">
                  Quelle: Towards AI
                </a>
              </div>
							<div class="px-6 py-4 bg-gray-100">
								<div class="font-bold text-2xl mb-2">1970er: KI und ML trennen sich</div>
								<p class="text-gray-700 text-base">
									In den späten 1970er und frühen 1980er Jahren konzentrierte sich die Forschung im Bereich der künstlichen Intelligenz mehr auf die 
                  Verwendung logischer, wissensbasierter Ansätze als auf Algorithmen, und die Erforschung neuronaler Netzwerke wurde von Informatik- und KI-Forschern 
                  aufgegeben. Dies führte zu einer Spaltung zwischen KI und Machine Learning, welche bis dahin als Trainingsprogramm für KI verwendet wurde.
                  Das Ziel der ML-Industrie verlagerte sich von der Ausbildung für künstliche Intelligenz zur Lösung praktischer Probleme, wobei die ML-Industrie ihren 
                  Fokus auf neuronale Netze behielt und dann in den 1990er Jahren florierte. Der größte Teil dieses Erfolgs war auf das Wachstum des Internets zurückzuführen, 
                  das von der ständig wachsenden Verfügbarkeit digitaler Daten und der Möglichkeit profitierte, seine Dienste über das Internet zu teilen.
								</p>
							</div>
							<div class="flex flex-col gap-4 px-6 pt-4 pb-4 bg-gray-100">
								<div>
									<span
										class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
									>
										Künstliche Intelligenz
									</span>
									<span
										class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
									>
										Machine Learning
									</span>
								</div>
								<div>
									<form action="https://towardsai.net/p/machine-learning/differences-between-ai-and-machine-learning-1255b182fc6">
										<button
											type="submit"
											class="inline-block px-4 py-1.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
											data-mdb-ripple="true"
										>
											Read more
										</button>
									</form>
								</div>
							</div>
						</div>
					</div>
				</li>
				<li>
					<div class="md:flex flex-start">
						<div class="bg-blue-600 w-6 h-6 flex items-center justify-center rounded-full -ml-3">
							<svg
								aria-hidden="true"
								focusable="false"
								data-prefix="fas"
								class="text-white w-3 h-3"
								role="img"
								xmlns="http://www.w3.org/2000/svg"
								viewBox="0 0 448 512"
							>
								<path
									fill="currentColor"
									d="M0 464c0 26.5 21.5 48 48 48h352c26.5 0 48-21.5 48-48V192H0v272zm64-192c0-8.8 7.2-16 16-16h288c8.8 0 16 7.2 16 16v64c0 8.8-7.2 16-16 16H80c-8.8 0-16-7.2-16-16v-64zM400 64h-48V16c0-8.8-7.2-16-16-16h-32c-8.8 0-16 7.2-16 16v48H160V16c0-8.8-7.2-16-16-16h-32c-8.8 0-16 7.2-16 16v48H48C21.5 64 0 85.5 0 112v48h448v-48c0-26.5-21.5-48-48-48z"
								/>
							</svg>
						</div>
						<div class="max-w-md rounded overflow-hidden shadow-lg ml-6 mb-6">
              <div class="relative group">
                <img
                  class="w-full block h-auto"
                  src="../../../static/boosting.jpg"
                  alt="Boosting"
                />
                <a href="https://www.ecmwf.int/sites/default/files/Ai-image-deep-net-v3-690px.jpg" target="_blank" class="opacity-0 bottom-0 absolute text-left group-hover:opacity-80 w-full border-[0.5px] rounded-t bg-gray-200 text-gray-700 px-6 py-1">
                  Quelle: ECMWF
                </a>
              </div>
							<div class="px-6 py-4 bg-gray-100">
								<div class="font-bold text-2xl mb-2">1990: Boosting-Algorithmen</div>
								<p class="text-gray-700 text-base">
									Boosting-Algorithmen reduzieren Vorurteile während des Supervised Learning und beinhalten ML-Algorithmen, die schwache Lernende in starke verwandeln. 
                  Dieses Konzept wurde erstmals 1990 in einem Artikel mit dem Titel „The Strength of Weak Learnability“ von Robert Schapire vorgestellt. 
                  Schapire argumentiert: „Eine Gruppe schwacher Lernender kann einen einzigen starken Lernenden hervorbringen.“ wobei schwache Lernende als Klassifikatoren 
                  definiert werden, die nur geringfügig mit der wahren Klassifikation korrelieren, und ein starker Lernender leicht klassifiziert und gut auf die wahre 
                  Klassifikation ausgerichtet ist. „Boosting“ gilt als notwendige Weiterentwicklung für die Evolution des maschinellen Lernens.
								</p>
							</div>
							<div class="flex flex-col gap-4 px-6 pt-4 pb-4 bg-gray-100">
								<div>
									<span
										class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
									>
										Supervised learning
									</span>
									<span
										class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
									>
										Robert Schapire
									</span>
								</div>
								<div>
									<form action="https://de.wikipedia.org/wiki/Boosting#:~:text=Boosting%20(engl.,einem%20einzigen%20guten%20Klassifikator%20verschmilzt.">
										<button
											type="submit"
											class="inline-block px-4 py-1.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
											data-mdb-ripple="true"
										>
											Read more
										</button>
									</form>
								</div>
							</div>
						</div>
					</div>
				</li>
				<li>
					<div class="md:flex flex-start">
						<div class="bg-blue-600 w-6 h-6 flex items-center justify-center rounded-full -ml-3">
							<svg
								aria-hidden="true"
								focusable="false"
								data-prefix="fas"
								class="text-white w-3 h-3"
								role="img"
								xmlns="http://www.w3.org/2000/svg"
								viewBox="0 0 448 512"
							>
								<path
									fill="currentColor"
									d="M0 464c0 26.5 21.5 48 48 48h352c26.5 0 48-21.5 48-48V192H0v272zm64-192c0-8.8 7.2-16 16-16h288c8.8 0 16 7.2 16 16v64c0 8.8-7.2 16-16 16H80c-8.8 0-16-7.2-16-16v-64zM400 64h-48V16c0-8.8-7.2-16-16-16h-32c-8.8 0-16 7.2-16 16v48H160V16c0-8.8-7.2-16-16-16h-32c-8.8 0-16 7.2-16 16v48H48C21.5 64 0 85.5 0 112v48h448v-48c0-26.5-21.5-48-48-48z"
								/>
							</svg>
						</div>
						<div class="max-w-md rounded overflow-hidden shadow-lg ml-6 mb-6">
              <div class="relative group">
                <img
                  class="w-full block h-auto"
                  src="../../../static/speechrecog.jpg"
                  alt="Spracherkennung"
                />
                <a href="https://recfaces.com/articles/what-is-voice-recognition" target="_blank" class="opacity-0 bottom-0 absolute text-left group-hover:opacity-80 w-full border-[0.5px] rounded-t bg-gray-200 text-gray-700 px-6 py-1">
                  Quelle: Recfaces
                </a>
              </div>
							<div class="px-6 py-4 bg-gray-100">
								<div class="font-bold text-2xl mb-2">1997: Spracherkennungssysteme</div>
								<p class="text-gray-700 text-base">
									1997 beschrieben Jürgen Schmidhuber und Sepp Hochreite ein neuronales Netzwerkmodell namens Long Short-Term Memory (LSTM), 
                  das derzeit zum Trainieren vieler Spracherkennungssysteme verwendet wird. LSTM kann Aufgaben lernen, die die Erinnerung an Ereignisse 
                  erfordern, die Tausende von diskreten Schritten zuvor stattgefunden haben.
                  Im Jahr 2015 hatte das Spracherkennungsprogramm von Google Berichten zufolge einen signifikanten Leistungssprung von 49 Prozent, indem 
                  es ein von Connectionist Temporal Classification (CTC) trainiertes LSTM verwendete, eine Art neuronaler Netzwerkausgabe und Bewertungsfunktion, 
                  um Sequenzprobleme anzugehen, bei denen Zeit eine Variable ist.
								</p>
							</div>
							<div class="flex flex-col gap-4 px-6 pt-4 pb-4 bg-gray-100">
								<div>
									<span
										class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
									>
										Google Spracherkennung
									</span>
									<span
										class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
									>
                    Neuronale Netze
									</span>
								</div>
								<div>
									<form action="https://de.wikipedia.org/wiki/Long_short-term_memory">
										<button
											type="submit"
											class="inline-block px-4 py-1.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
											data-mdb-ripple="true"
										>
											Read more
										</button>
									</form>
								</div>
							</div>
						</div>
					</div>
				</li>

				<li>
					<div class="md:flex flex-start">
						<div class="bg-blue-600 w-6 h-6 flex items-center justify-center rounded-full -ml-3">
							<svg
								aria-hidden="true"
								focusable="false"
								data-prefix="fas"
								class="text-white w-3 h-3"
								role="img"
								xmlns="http://www.w3.org/2000/svg"
								viewBox="0 0 448 512"
							>
								<path
									fill="currentColor"
									d="M0 464c0 26.5 21.5 48 48 48h352c26.5 0 48-21.5 48-48V192H0v272zm64-192c0-8.8 7.2-16 16-16h288c8.8 0 16 7.2 16 16v64c0 8.8-7.2 16-16 16H80c-8.8 0-16-7.2-16-16v-64zM400 64h-48V16c0-8.8-7.2-16-16-16h-32c-8.8 0-16 7.2-16 16v48H160V16c0-8.8-7.2-16-16-16h-32c-8.8 0-16 7.2-16 16v48H48C21.5 64 0 85.5 0 112v48h448v-48c0-26.5-21.5-48-48-48z"
								/>
							</svg>
						</div>
						<div class="max-w-md rounded overflow-hidden shadow-lg ml-6 mb-6">
              <div class="relative group">
                <img
                  class="w-full block h-auto"
                  src="../../../static/facerecog.jpeg"
                  alt="Gesichtserkennung"
                />
                <a href="https://www.handelskraft.de/face-recognition-gruseltechnologie-oder-tor-zur-neuen-payment-welt/" target="_blank" class="opacity-0 bottom-0 absolute text-left group-hover:opacity-80 w-full border-[0.5px] rounded-t bg-gray-200 text-gray-700 px-6 py-1">
                  Quelle: Handelskraft
                </a>
              </div>
							<div class="px-6 py-4 bg-gray-100">
								<div class="font-bold text-2xl mb-2">2006: Bessere Gesichtserkennungsalgorithmen</div>
								<p class="text-gray-700 text-base">
									Gesichtserkennung ist eine Erkennungstechnik, die verwendet wird, um im Datensatz gespeicherte Gesichter zu erkennen. Es identifiziert ein Gesicht durch 
                  Vergleichen und Analysieren von Mustern basierend auf Gesichtskonturen durch trainierte neuronale Netzwerkmodelle. Im Jahr 2006 führte die 
                  Face Recognition Grand Challenge eine Bewertung der Gesichtserkennungsalgorithmen durch, und das Ergebnis der Bewertung ergab, dass die neuen Algorithmen 
                  zehnmal genauer waren als die Gesichtserkennungsalgorithmen von 2002 und 100-mal genauer als die von 1995. Einige der Algorithmen waren dazu in der Lage 
                  menschliche Teilnehmer bei der Erkennung von Gesichtern übertreffen und eineiige Zwillinge eindeutig identifizieren könnten.
								</p>
							</div>
							<div class="flex flex-col gap-4 px-6 pt-4 pb-4 bg-gray-100">
								<div>
									<span
										class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
									>
										Gesichtserkennung
									</span>
									<span
										class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
									>
										Neuronales Netzwerkmodell
									</span>
								</div>
								<div>
									<form action="https://www.internetjustsociety.org/cosmonaut/facial-recognition-an-introduction">
										<button
											type="submit"
											class="inline-block px-4 py-1.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
											data-mdb-ripple="true"
										>
											Read more
										</button>
									</form>
								</div>
							</div>
						</div>
					</div>
				</li>

				<li>
					<div class="md:flex flex-start">
						<div class="bg-blue-600 w-6 h-6 flex items-center justify-center rounded-full -ml-3">
							<svg
								aria-hidden="true"
								focusable="false"
								data-prefix="fas"
								class="text-white w-3 h-3"
								role="img"
								xmlns="http://www.w3.org/2000/svg"
								viewBox="0 0 448 512"
							>
								<path
									fill="currentColor"
									d="M0 464c0 26.5 21.5 48 48 48h352c26.5 0 48-21.5 48-48V192H0v272zm64-192c0-8.8 7.2-16 16-16h288c8.8 0 16 7.2 16 16v64c0 8.8-7.2 16-16 16H80c-8.8 0-16-7.2-16-16v-64zM400 64h-48V16c0-8.8-7.2-16-16-16h-32c-8.8 0-16 7.2-16 16v48H160V16c0-8.8-7.2-16-16-16h-32c-8.8 0-16 7.2-16 16v48H48C21.5 64 0 85.5 0 112v48h448v-48c0-26.5-21.5-48-48-48z"
								/>
							</svg>
						</div>
						<div class="max-w-md rounded overflow-hidden shadow-lg ml-6 mb-6">
							<div class="relative group">
                <img
                  class="w-full block h-auto"
                  src="../../../static/mljetzt.jpg"
                  alt="ML Jetzt vs Zukunft"
                />
                <a href="https://www.informatec.com/en/machine-learning" target="_blank" class="opacity-0 bottom-0 absolute text-left group-hover:opacity-80 w-full border-[0.5px] rounded-t bg-gray-200 text-gray-700 px-6 py-1 ">
                  Quelle: Informatec
                </a>
              </div>
							<div class="px-6 py-4 bg-gray-100">
								<div class="font-bold text-2xl mb-2">2006-20xx: ML Jetzt vs. Zukunft</div>
								<p class="text-gray-700 text-base">
									Die Standford University definierte Machine Learning als „die Wissenschaft, Computer zum Handeln zu bringen, ohne explizit programmiert zu werden“. 
                  ML war der Schlüssel für einige der bedeutendsten technologischen Fortschritte. Es wird für die neue Industrie der selbstfahrenden Fahrzeuge, 
                  für die Erforschung der Galaxie und in Unternehmen eingesetzt. Einige häufige Aufgaben, die in der Geschäftswelt ML eingesetzt werden, sind: 
                  Verkaufsdatenanalyse, Produktempfehlungen, dynamische Preisgestaltung und mehr.<br> Klar ist, dass ML auch in Zukunft im Mittelpunkt unseres Lebens stehen wird. 
                  Google arbeitet derzeit an einem Projekt zum maschinellen Lernen mit einem Ansatz namens Feinabstimmung von Anweisungen. Sie zielen darauf ab, ein ML-Modell 
                  zu trainieren, um Probleme bei der Verarbeitung natürlicher Sprache auf allgemeine Weise zu lösen.
								</p>
							</div>
							<div class="flex flex-col gap-4 px-6 pt-4 pb-4 bg-gray-100">
								<div>
									<span
										class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
									>
										Geschäftswelt und Technologie
									</span>
									<span
										class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
									>
                    Autonomes Fahren
									</span>
								</div>
								<div>
									<form action="http://mlclass.stanford.edu/#:~:text=Machine%20learning%20is%20the%20science,understanding%20of%20the%20human%20genome.">
										<button
											type="submit"
											class="inline-block px-4 py-1.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
											data-mdb-ripple="true"
										>
											Read more
										</button>
									</form>
								</div>
							</div>
						</div>
					</div>
				</li>
			</ol>
		</div>
	</div>

	<div id="part-three" class="mt-32">
		<h1 class="headline text-4xl font-bold mb-12 ml-24 uppercase text-gray-100">
			3. Die Arten von ML
		</h1>
    <div class="flex flex-col mt-8 mb-28 justify-center items-center text-center">
      <span class="text-2xl w-3/4 text-justify leading-relaxed mb-6 text-gray-300">
        Es gibt verschiedene Möglichkeiten, ML-Algorithmen zu trainieren, jede mit ihren eigenen Vor- und Nachteilen.
      </span>
    </div>

		<div class="flex flex-col w-full gap-y-60 items-center">
			<InformationTile
				title="Supervised Learning"
				content="Beim Supervised Learning erhält der ML-Algorithmus einen kleinen und beschrifteten Trainingsdatensatz eines größeren Datensatzes, 
        mit dem er arbeiten kann. Dies soll dem Algorithmus eine Grundidee des Problems, der Lösung und der zu behandelnden Datenpunkte geben. 
        Der Algorithmus findet dann Beziehungen zwischen den gegebenen Parametern und hat eine Vorstellung davon, wie die Daten funktionieren und 
        die Beziehung zwischen Eingabe und Ausgabe. Dann wird es auf dem endgültigen Datensatz eingesetzt, wo der Algorithmus mehr lernt und neue 
        Muster und Beziehungen entdeckt, während er sich auf dem endgültigen Datensatz trainiert."
				class="mt-20"
			>
				<div slot="right_slot">
					<AnimationContainer from_right>
						<img src="../../../static/supervised.jpg" alt="vikus_viewer" class="rounded-3xl shadow-2xl" />
					</AnimationContainer>
				</div>
			</InformationTile>
			<InformationTile title="Unsupervised Learning" right_side class="mt-20">
				<div slot="content" class="text-gray-400 text-2xl text-justify">
          Beim Unsupervised Learning muss der Datensatz nicht maschinenlesbar gemacht oder von Entwicklern gekennzeichnet werden, sodass das Programm viel 
          größere Datensätze bearbeiten kann. Beim Unspervised Learning gibt es keine Gekennzeichnung, an denen das Programm abarbeiten, was zur Schaffung verborgener 
          Strukturen führt. Die Erstellung dieser verborgenen Strukturen hilft dem unbeaufsichtigten Lernen, sich an die Daten anzupassen, indem verborgene Strukturen dynamisch geändert werden.
				</div>
				<div slot="right_slot">
					<AnimationContainer>
						<img
							src="../../../static/unsupervised.jpg"
							alt="vikus_viewer"
							class="rounded-3xl shadow-2xl"
						/>
					</AnimationContainer>
				</div>
			</InformationTile>
      <InformationTile
      title="Reinforcement Learning"
      content="Beim Reinforcement Learning handelt es sich um einen Algorithmus, der sich selbst verbessert und anhand einer Trial-and-Error-Methode aus neuen Situationen lernt.
      Es wird mit einem Interpreter und einem Belohnungssystem eingesetzt. Bei jeder Iteration des Algorithmus wird das Ausgabeergebnis an den Interpreter übergeben, der 
      entscheidet, ob das Ergebnis gültig ist oder nicht. Falls das Programm die richtige Lösung findet, akzeptiert der Interpreter die Lösung, indem er dem Algorithmus eine Belohnung bereitstellt. 
      Wenn das Ergebnis nicht gültig ist, muss der Algorithmus wiederholen, bis er ein besseres Ergebnis findet."
      class="mt-20"
    >
      <div slot="right_slot">
        <AnimationContainer from_right>
          <img src="../../../static/reward.jpg" alt="vikus_viewer" class="rounded-3xl shadow-2xl" />
        </AnimationContainer>
      </div>
    </InformationTile>
		</div>

		<section class="mb-32 mx-6 mt-48 text-gray-100 text-center bg-gray-800 rounded-2xl p-6">
			<div class="flex justify-center">
				<div class="text-center w-1/2">
					<h2 class="text-6xl font-bold mb-6 text-center">4 Übersicht der wichtigsten ML Begriffe</h2>
					<p class="text-2xl text-gray-400 mb-12">
            Hier wird auf einige wichtige Begriffe im Bereich ML eingegangen:
				</div>
			</div>

			<div
				class="grid bg-gray-700 rounded-2xl shadow-2xl p-6 md:grid-cols-2 lg:grid-cols-4 lg:gap-x-12"
			>
				<div class="mb-12 lg:mb-0">
					<div class="p-4 bg-blue-600 rounded-full shadow-lg inline-block mb-6">
						<Icon icon="tablet" size="24px" />
					</div>
					<h5 class="text-2xl font-bold mb-4">Deep Learning</h5>
					<p class="text-xl text-justify text-gray-300">
						Deep Learning ist eine Anwendung von ML. Deep-Learning-Netzwerke interpretieren Big Data, sowohl unstrukturiert als auch strukturiert, 
            und erkennen Muster in den Daten. Je mehr Daten sie trainieren und aus denen sie lernen können, desto fundierter und genauer werden ihre Entscheidungen sein.
            Ein reales Beispiel dafür wäre Chatbox, je mehr Daten es trainiert, desto besser funktioniert es.
					</p>
				</div>

				<div class="mb-12 lg:mb-0">
					<div class="p-4 bg-blue-600 rounded-full shadow-lg inline-block mb-6">
						<Icon icon="slack" size="24px" />
					</div>
					<h5 class="text-2xl font-bold mb-4">Neuronale Netzwerke</h5>
					<p class="text-xl text-justify text-gray-300">
            Neuronale Netze sind eng mit Deep Learning verwandt. Seine Aufgabe ist es, sequentielle Schichten von Neuronen zu erstellen, die das 
            Verständnis der von einer Maschine gesammelten Daten vertiefen, um eine genaue Analyse zu ermöglichen.
            Ein neuronales Netzwerk besteht aus Schichten von Knoten, denen dann durch Koeffizienten eine Gewichtung zugewiesen, 
            und das Netzwerk analysiert wird.
					</p>
				</div>

				<div class="mb-12 md:mb-0">
					<div class="p-4 bg-blue-600 rounded-full shadow-lg inline-block mb-6">
						<Icon icon="user" size="24px" />
					</div>
					<h5 class="text-2xl font-bold mb-4">Regression</h5>
					<p class="text-xl text-justify text-gray-300">
						Regressionen in ML werden verwendet, um Beziehungen und Korrelationen zwischen verschiedenen Datentypen herzustellen.
            Regressionen können nützlich sein, wenn Ergebnisse basierend auf Daten in der Gegenwart vorhergesagt werden. Wenn sich 
            beispielsweise ein Produkt bei einer bestimmten Personengruppe gut verkauft, kann das Geschäft in Gebieten, in denen diese 
            Personen leben, mehr von diesem Produkt anbieten.
					</p>
				</div>

				<div class="mb-12 md:mb-0">
					<div class="p-4 bg-blue-600 rounded-full shadow-lg inline-block mb-6">
						<Icon icon="users" size="24px" />
					</div>
					<h5 class="text-2xl font-bold mb-4">Clustering</h5>
					<p class="text-xl text-justify text-gray-300">
						Clustering, bei dem Datenpunkte nach Merkmalen und Attributen gruppiert werden, ist eine Form des unüberwachten Lernens.
            Clustering kann in mehreren Geschäftsbereichen verwendet werden, z. B. um Kundendemografie und Kaufverhalten in bestimmte 
            Segmente für Targeting und Produktpositionierung zu organisieren.
					</p>
				</div>
			</div>
		</section>
	</div>

  <div id="part-five" class="grid mt-32">
    <h1 class="headline text-4xl font-bold mb-12 ml-24 uppercase text-gray-100">
      5. Anwendungsgebiete
    </h1>

    <div class="grid justify-center items-center justify-self-center w-3/4">
      <div class="grid gap-12 m-6 sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
      
        <div
        class="max-w-sm grid grid-rows-2 rounded-lg border shadow-md bg-gray-800 border-gray-700"
        >
          <img
            class="rounded-t-lg h-full"
            src="../../../static/Suchmaschine.jpg"
            alt=""
          />
          <div class="p-5  grid content-between row-span-2">
            <h5 class="mb-2 text-2xl font-bold tracking-tight text-white">
              Suchmaschinen
            </h5>
            <p class="mb-3 font-normal text-gray-400">
              ML ermöglicht es uns, die riesigen Datenmengen des Internets zu erforschen und
              relevante Inhalte bereitzustellen.
            </p>
            <a
              href="#part-one"
              class="inline-flex items-center w-fit py-2 px-3 text-sm font-medium text-center text-white rounded-lg focus:ring-4 focus:outline-none bg-blue-600 hover:bg-blue-700 focus:ring-blue-800"
            >
              Read more
              <svg
                class="ml-2 -mr-1 w-4 h-4"
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
                ><path
                  fill-rule="evenodd"
                  d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
                  clip-rule="evenodd"
                /></svg
              >
            </a>
          </div>
        </div>
        <div
        class="max-w-sm grid grid-rows-2 rounded-lg border shadow-md bg-gray-800 border-gray-700"
        >
          <img class="rounded-t-lg h-full" src="../../../static/Sprachassistenten.jpg" alt="" />
          <div class="p-5  grid content-between row-span-2">
            <h5 class="mb-2 text-2xl font-bold tracking-tight text-white">
              Sprachassistenten
            </h5>
            <p class="mb-3 font-normal text-gray-400">
              Sprachassistenten können die aufgenommenen Geräusche in Wörter übersetzen, diese mit
              natürlicher Sprachverarbeitung verstehen und so Aufgaben erfüllen.
            </p>
            <a
              href="#part-one"
              class="inline-flex items-center w-fit py-2 px-3 text-sm font-medium text-center text-white rounded-lg focus:ring-4 focus:outline-none bg-blue-600 hover:bg-blue-700 focus:ring-blue-800"
            >
              Read more
              <svg
                class="ml-2 -mr-1 w-4 h-4"
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
                ><path
                  fill-rule="evenodd"
                  d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
                  clip-rule="evenodd"
                /></svg
              >
            </a>
          </div>
        </div>
        <div
        class="max-w-sm grid grid-rows-2 rounded-lg border shadow-md bg-gray-800 border-gray-700"
        >
          <img
            class="rounded-t-lg h-full"
            src="../../../static/Empfehlungsdienste.jpg"
            alt=""
          />
          <div class="p-5  grid content-between row-span-2">
            <h5 class="mb-2 text-2xl font-bold tracking-tight text-white">
              Social Media
            </h5>

            <p class="mb-3 font-normal text-gray-400">
              Die Algorithmen hinter den Empfehlungssystemen von Social Media werden alle
              ML-basiert. Sie lernen von dem Nutzerverhalten und passen so den Feed an.
            </p>
            <a
              href="#part-one"
              class="inline-flex items-center w-fit py-2 px-3 text-sm font-medium text-center text-white rounded-lg focus:ring-4 focus:outline-none bg-blue-600 hover:bg-blue-700 focus:ring-blue-800"
            >
              Read more
              <svg
                class="ml-2 -mr-1 w-4 h-4"
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
                ><path
                  fill-rule="evenodd"
                  d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
                  clip-rule="evenodd"
                /></svg
              >
            </a>
          </div>
        </div>
      
        <div
        class="max-w-sm grid grid-rows-2 rounded-lg border shadow-md bg-gray-800 border-gray-700"
        >
          <img class="rounded-t-lg h-full" src="../../../static/Personal_Content.jpg" alt="" />
          <div class="p-5  grid content-between row-span-2">
            <h5 class="mb-2 text-2xl font-bold tracking-tight text-white">
              Persönliche Inhalte
            </h5>
            <p class="mb-3 font-normal text-gray-400">
              Ob Werbungen oder vorgeschlagene Sucheinträge - ML Algorithmen analysieren das Nutzerverhalten
              im Internet und schlagen so personalisierte Inhalte vor.
            </p>
            <a
              href="#part-one"
              class="inline-flex items-center w-fit py-2 px-3 text-sm font-medium text-center text-white rounded-lg focus:ring-4 focus:outline-none bg-blue-600 hover:bg-blue-700 focus:ring-blue-800"
            >
              Read more
              <svg
                class="ml-2 -mr-1 w-4 h-4"
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
                ><path
                  fill-rule="evenodd"
                  d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
                  clip-rule="evenodd"
                /></svg
              >
            </a>
          </div>
        </div>
        <div
        class="max-w-sm grid grid-rows-2 rounded-lg border shadow-md bg-gray-800 border-gray-700"
        >
          <img class="rounded-t-lg h-full" src="../../../static/Chatbot.jpg" alt="" />
          <div class="p-5  grid content-between row-span-2">
            <h5 class="mb-2 text-2xl font-bold tracking-tight text-white">
              Chatbot
            </h5>
            <p class="mb-3 font-normal text-gray-400">
              Besonders beim Kundenservice und -support setzen Unternehmen auf Chatbots, die die
              wichtigsten Informationen des Kundenproblems erfragen und analysieren.
            </p>
            <a
              href="#part-one"
              class="inline-flex items-center w-fit py-2 px-3 text-sm font-medium text-center text-white rounded-lg focus:ring-4 focus:outline-none bg-blue-600 hover:bg-blue-700 focus:ring-blue-800"
            >
              Read more
              <svg
                class="ml-2 -mr-1 w-4 h-4"
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
                ><path
                  fill-rule="evenodd"
                  d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
                  clip-rule="evenodd"
                /></svg
              >
            </a>
          </div>
        </div>
        <div
        class="max-w-sm grid grid-rows-2 rounded-lg border shadow-md bg-gray-800 border-gray-700"
        >
          <img class="rounded-t-lg h-full" src="../../../static/Content-Moderation.jpg" alt="" />
          <div class="p-5  grid content-between row-span-2">
            <h5 class="mb-2 text-2xl font-bold tracking-tight text-white">
              Inhaltsverwaltung
            </h5>
            <p class="mb-3 font-normal text-gray-400">
              Die Inhaltsverwaltung in den sozialen Medien stellt die Anbieter vor große
              Herausforderungen. ML Algorithmen untersützen dabei, Hasskomentare o.Ä. zu identifizieren und
              zu löschen.
            </p>
            <a
              href="#part-one"
              class="inline-flex items-center w-fit py-2 px-3 text-sm font-medium text-center text-white rounded-lg focus:ring-4 focus:outline-none bg-blue-600 hover:bg-blue-700 focus:ring-blue-800"
            >
              Read more
              <svg
                class="ml-2 -mr-1 w-4 h-4"
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
                ><path
                  fill-rule="evenodd"
                  d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
                  clip-rule="evenodd"
                /></svg
              >
            </a>
          </div>
        </div>
        <div
        class="max-w-sm grid grid-rows-2 rounded-lg border shadow-md bg-gray-800 border-gray-700"
        >
          <img class="rounded-t-lg h-full" src="../../../static/Gesichtserkennung.jpg" alt="" />
          <div class="p-5  grid content-between row-span-2">
            <h5 class="mb-2 text-2xl font-bold tracking-tight text-white">
              Gesichtserkennung
            </h5>
            <p class="mb-3 font-normal text-gray-400">
              Sowohl in Smartphone-Kameras als auch in Überwachungskameras kommen ML Algorithmen zum Einsatz,
              um Gesichter und weitere Informationen zu erkennen.
            </p>
            <a
              href="#part-one"
              class="inline-flex items-center w-fit py-2 px-3 text-sm font-medium text-center text-white rounded-lg focus:ring-4 focus:outline-none bg-blue-600 hover:bg-blue-700 focus:ring-blue-800"
            >
              Read more
              <svg
                class="ml-2 -mr-1 w-4 h-4"
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
                ><path
                  fill-rule="evenodd"
                  d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
                  clip-rule="evenodd"
                /></svg
              >
            </a>
          </div>
        </div>
        <div
          class="max-w-sm grid grid-rows-2 rounded-lg border shadow-md bg-gray-800 border-gray-700"
        >
          <img class="rounded-t-lg h-full" src="../../../static/Mobilität.jpg" alt="" />
          <div class="p-5  grid content-between row-span-2">
            <h5 class="mb-2 text-2xl font-bold tracking-tight text-white">
              Mobilität
            </h5>
            <p class="mb-3 font-normal text-gray-400">
              Autonome Fahrzeuge sind nur die Spitze des Eisberges - ML Algorithmen unterstützt den Fahrer
              auch mit Einparkhilfen oder dem Halten der Fahrspur.
            </p>
            <a
              href="#part-one"
              class="inline-flex items-center w-fit py-2 px-3 text-sm font-medium text-center text-white rounded-lg focus:ring-4 focus:outline-none bg-blue-600 hover:bg-blue-700 focus:ring-blue-800"
            >
              Read more
              <svg
                class="ml-2 -mr-1 w-4 h-4"
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
                ><path
                  fill-rule="evenodd"
                  d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
                  clip-rule="evenodd"
                /></svg
              >
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>

	<div class="flex gap-16 w-full place-self-center items-center justify-center bg-gray-100 shadow-lg">
		<div
			class="text-7xl font-sans leading-snug text-center font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-500 to-teal-500 drop-shadow-lg"
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
			<div class="w-full text-center m-6 p-8">
				<img
					src="https://images.t3n.de/news/wp-content/uploads/2022/03/Anonymous-Maske-1.jpg?class=hero"
					class="rounded-full w-32 mb-4 mx-auto"
					alt="Avatar"
				/>
				<h5 class="text-xl font-medium leading-tight mb-2">Hamid Omar</h5>
				<p class="text-gray-500 mb-2">Web designer</p>
				<ul class="list-inside flex mx-auto justify-center">
					<a href="#!" class="px-2">
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
					<a href="#!" class="px-2">
						<svg
							xmlns="http://www.w3.org/2000/svg"
							viewBox="0 0 512 512"
							class="w-4 h-4 text-blue-600"
						>
							<path
								fill="currentColor"
								d="M459.37 151.716c.325 4.548.325 9.097.325 13.645 0 138.72-105.583 298.558-298.558 298.558-59.452 0-114.68-17.219-161.137-47.106 8.447.974 16.568 1.299 25.34 1.299 49.055 0 94.213-16.568 130.274-44.832-46.132-.975-84.792-31.188-98.112-72.772 6.498.974 12.995 1.624 19.818 1.624 9.421 0 18.843-1.3 27.614-3.573-48.081-9.747-84.143-51.98-84.143-102.985v-1.299c13.969 7.797 30.214 12.67 47.431 13.319-28.264-18.843-46.781-51.005-46.781-87.391 0-19.492 5.197-37.36 14.294-52.954 51.655 63.675 129.3 105.258 216.365 109.807-1.624-7.797-2.599-15.918-2.599-24.04 0-57.828 46.782-104.934 104.934-104.934 30.213 0 57.502 12.67 76.67 33.137 23.715-4.548 46.456-13.32 66.599-25.34-7.798 24.366-24.366 44.833-46.132 57.827 21.117-2.273 41.584-8.122 60.426-16.243-14.292 20.791-32.161 39.308-52.628 54.253z"
							/>
						</svg>
					</a>
					<a href="#!" class="px-2">
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

<style lang="postcss"></style>