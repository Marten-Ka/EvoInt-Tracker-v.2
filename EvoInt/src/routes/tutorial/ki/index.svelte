<script lang="ts">
	import TutorialRedirectButton from '../../../components/_TutorialRedirectButton.svelte';
	import AnimationContainer from '../../../components/AnimationContainer.svelte';
	import Footer from '../../../components/Footer.svelte';
	import Header from '../../../components/Header.svelte';
	import InformationTile from '../../../components/InformationTile.svelte';
	import Icon from '../../../components/Icon.svelte';

	const redirects = [
		{ text: '1. Der Begriff der Künstlichen Intelligenz', href: '#part-one', icon: 'terminal' },
		{ text: '2. Die historische Entwicklung von KI', href: '#part-two', icon: 'terminal' },
		{ text: '3. Die Arten von KI', href: '#part-three', icon: 'terminal' },
		{ text: '4. Übersicht der wichtigsten Begriffe', href: '#part-four', icon: 'terminal' },
		{ text: '5. Anwendungsgebiete', href: '#part-five', icon: 'terminal' },
		{ text: '6. Fazit', href: '#part-six', icon: 'terminal' }
	];
</script>

<Header />

<div class="flex flex-col text-center justify-center items-center mt-20">
	<h1
		class="headline text-7xl font-bold uppercase text-gray-100 [text-shadow:0_4px_8px_rgba(255,255,255,0.25)]"
	>
		Künstliche Intelligenz
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
			1. Der Begriff der Künstlichen Intelligenz
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
									src="https://profile-images.xing.com/images/8532834afc356e7b294a609cc06ae98e-3/inis-ehrlich.1024x1024.jpg"
									class="rounded-full shadow-md"
									alt="Inis Ehrlich"
								/>
							</div>
							<div class="md:ml-6 place-self-center">
								<p class="text-gray-500 text-xl font-semibold italic mb-6">
									"Die KI, einfach erklärt, ist der Versuch, menschliches Lernen und Denken auf den
									Computer zu übertragen und ihm damit Intelligenz zu verleihen."
								</p>
								<p class="font-semibold text-xl mb-2 text-gray-800">Inis Ehrlich</p>
								<p class="font-semibold text-gray-500 mb-0">
									Referentin für Künstliche Intelligenz
								</p>
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
									src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/John_McCarthy_Stanford.jpg/220px-John_McCarthy_Stanford.jpg"
									class="rounded-full shadow-md"
									alt="John McCartney"
								/>
							</div>
							<div class="md:ml-6 place-self-center">
								<p class="text-gray-500 text-xl font-semibold italic mb-6">
									"Es ist die Wissenschaft und Technik der Herstellung intelligenter Maschinen,
									insbesondere intelligenter Computerprogramme."
								</p>
								<p class="font-semibold text-xl mb-2 text-gray-800">John McCartney</p>
								<p class="font-semibold text-gray-500 mb-0">US-amerikanischer Informatiker</p>
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
									src="https://cdn.pixabay.com/photo/2014/01/27/18/13/europe-253311_1280.jpg"
									class="rounded-full shadow-md"
									alt="John McCartney"
								/>
							</div>
							<div class="md:ml-6 place-self-center">
								<p class="text-gray-500 text-xl font-semibold italic mb-6">
									"Künstliche Intelligenz ist die Fähigkeit einer Maschine, menschliche Fähigkeiten
									wie logisches Denken, Lernen, Planen und Kreativität zu imitieren."
								</p>
								<p class="font-semibold text-xl mb-2 text-gray-800">Europäisches Parlament</p>
								<p class="font-semibold text-gray-500 mb-0">US-amerikanischer Informatiker</p>
							</div>
						</div>
					</div>
				</div>
			</div>
		</section>

		<div class="flex flex-col justify-center items-center text-center">
			<!-- <div class="flex flex-col my-16 justify-center items-center text-center">
				<span
					class="text-2xl font-bold place-self-start leading-relaxed mb-6 w-2/3 text-gray-100 italic"
				>
					"Die KI, einfach erklärt, ist der Versuch, menschliches Lernen und Denken auf den Computer
					zu übertragen und ihm damit Intelligenz zu verleihen."
				</span>
				<span class="text-2xl font-bold place-self-start leading-relaxed w-2/3 text-gray-100">
					- Ehrlich, Inis
				</span>
			</div>

			<div class="flex flex-col my-16 justify-center items-center text-center">
				<span
					class="text-2xl font-bold place-self-end leading-relaxed mb-6 w-2/3 text-gray-100 italic"
				>
					"Es ist die Wissenschaft und Technik der Herstellung intelligenter Maschinen, insbesondere
					intelligenter Computerprogramme. Es ist verwandt mit der ähnlichen Aufgabe, Computer zu
					benutzen, um menschliche Intelligenz zu verstehen, aber KI muss sich nicht auf Methoden
					beschränken, die biologisch beobachtbar sind."
				</span>
				<span class="text-2xl font-bold place-self-end leading-relaxed w-2/3 text-gray-100">
					- McCartney, John
				</span>
			</div>

			<div class="flex flex-col my-16 justify-center items-center text-center">
				<span
					class="text-2xl font-bold place-self-start leading-relaxed mb-6 w-2/3 text-gray-100 italic"
				>
					"Künstliche Intelligenz ist die Fähigkeit einer Maschine, menschliche Fähigkeiten wie
					logisches Denken, Lernen, Planen und Kreativität zu imitieren."
				</span>
				<span class="text-2xl font-bold place-self-start leading-relaxed w-2/3 text-gray-100">
					- Europäisches Parlament
				</span>
			</div> -->

			<div class="flex flex-col mt-8 mb-28 justify-center items-center text-center">
				<span class="text-2xl w-3/4 text-justify leading-relaxed mb-6 text-gray-300">
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
		<h1 class="headline text-4xl font-bold mb-12 ml-24 uppercase text-gray-100">
			2. Die historische Entwicklung von KI
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
							<img
								class="w-full"
								src="https://anthrowiki.at/images/thumb/a/ad/Model_of_a_Turing_machine.jpg/375px-Model_of_a_Turing_machine.jpg"
								alt="Turingmaschine"
							/>
							<div class="px-6 py-4 bg-gray-100">
								<div class="font-bold text-2xl mb-2">1936: Turingmaschine</div>
								<p class="text-gray-700 text-base">
									Alan Turing, ein britischer Mathematiker, legte 1936 schon den Grundstein für das,
									was wir heute unter Künstlicher Intelligenz verstehen. Mit seinen Theorien konnte
									er beweisen, dass eine Rechenmaschine (auch bezeichnet als "Turingmaschine") in
									der Lage wäre, kognitive Prozesse auszuführen, sofern sich diese in mehrere kleine
									Schritte zerlegen und algorithmisch darstellen lassen.
								</p>
							</div>
							<div class="flex flex-col gap-4 px-6 pt-4 pb-4 bg-gray-100">
								<div>
									<span
										class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
									>
										Alan Turing
									</span>
									<span
										class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
									>
										Grundstein der KI
									</span>
								</div>
								<div>
									<form action="https://de.wikipedia.org/wiki/Turingmaschine">
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
							<img
								class="w-full"
								src="https://cyfuture.com/blog/wp-content/uploads/2020/04/Dartmouth-Conference-in-1956.jpg"
								alt="Dartmouth Conference"
							/>
							<div class="px-6 py-4 bg-gray-100">
								<div class="font-bold text-2xl mb-2">1956: Der Begriff "KI" entsteht</div>
								<p class="text-gray-700 text-base">
									1956 treffen sich Wissenschaftler zu einer Konferenz am Dartmouth College im
									US-Bundesstaat New Hampshire und debattieren über die Simulation von menschlicher
									Intelligenz durch Maschinen. John McCartney schlägt dafür den Begriff "Künstliche
									Intelligenz" vor. Während der Konferenz entsteht außerdem das erste KI-Programm
									der Welt - der "Logic Theorist", der es schafft, mehrere mathematische Lehrsätze
									zu beweisen.
								</p>
							</div>
							<div class="flex flex-col gap-4 px-6 pt-4 pb-4 bg-gray-100">
								<div>
									<span
										class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
									>
										Dartmouth Konferenz
									</span>
									<span
										class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
									>
										John McCartney
									</span>
								</div>
								<div>
									<form action="https://de.wikipedia.org/wiki/Dartmouth_Conference">
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
							<img
								class="w-full"
								src="https://moodswag.com/wp-content/uploads/2020/09/Eliza.jpg"
								alt="ELIZA"
							/>
							<div class="px-6 py-4 bg-gray-100">
								<div class="font-bold text-2xl mb-2">1966: Der erste Chatbot</div>
								<p class="text-gray-700 text-base">
									1966 entwickelt der deutsch-amerikanische Informatiker Joseph Weizenbaum vom
									Massachusetts Institute of Technology das Computerprogramm "ELIZA", welches mit
									Menschen kommunizieren kann. ELIZA kann mehrere Gesprächspartner simulieren, wie
									beispielsweise einen Psychotherapeuten. Jedoch sind die genutzten Mittel zur
									Simulation des Gesprächs noch recht rudimentär geskriptet.
								</p>
							</div>
							<div class="flex flex-col gap-4 px-6 pt-4 pb-4 bg-gray-100">
								<div>
									<span
										class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
									>
										Joseph Weizenbaum
									</span>
									<span
										class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
									>
										ELIZA
									</span>
								</div>
								<div>
									<form action="https://de.wikipedia.org/wiki/ELIZA">
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
							<img
								class="w-full"
								src="https://www.bibliomedmanager.de/fileadmin/user_upload/alle-Portale/Bilder/TANGO/sp/2018/04/gettyimages_894319072.jpg"
								alt="MYCIN"
							/>
							<div class="px-6 py-4 bg-gray-100">
								<div class="font-bold text-2xl mb-2">1972: KI gelangt in die Medizin</div>
								<p class="text-gray-700 text-base">
									Die KI ist für viele schon lange kein Fremdwort mehr, doch jetzt findet sie ihren
									ersten Einsatz in der realen Welt. Das von Ted Shortlife an der Stanford
									University entwickelte Expertensystem "MYCIN" wird zur Diagnose und Therapie von
									Infektionskrankheiten eingesetzt. Doch auch wenn das System hohe Trefferquoten
									erzielt, erlangte es nicht die Bedeutung in der Medizin, die man sich erhofft
									hatte. Die Bereitschaft gegenüber solchen Systemen war schlicht zu gering, als
									dass sich Ärzte auf dessen Diagnose verlassen wollten.
								</p>
							</div>
							<div class="flex flex-col gap-4 px-6 pt-4 pb-4 bg-gray-100">
								<div>
									<span
										class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
									>
										MYCIN
									</span>
									<span
										class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
									>
										Praxiseinsatz
									</span>
								</div>
								<div>
									<form action="https://de.wikipedia.org/wiki/Mycin_(Expertensystem)">
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
							<img
								class="w-full"
								src="https://fscl01.fonpit.de/userfiles/7611461/image/AI-artificial-intelligence-robot/AI-robot_12-w810h462.jpg"
								alt="NETtalk"
							/>
							<div class="px-6 py-4 bg-gray-100">
								<div class="font-bold text-2xl mb-2">1986: Computer lernt sprechen</div>
								<p class="text-gray-700 text-base">
									Terrence J. Sejnowski und Charles Rosenberg bringen ihrem Programm "NETtalk"
									mithilfe von Beispielsätzen und Phonemketten das Sprechen bei. „NETtalk“ kann
									Wörter lesen und korrekt aussprechen sowie das Gelernte auf ihm unbekannte Wörter
									anwenden. Aufgrund dieser Fähigkeit, die darauf beruht, dass das Programm mit
									großen Datenmengen befüllt wird und daraus eigene Schlüsse zieht, gehört es
									ebenfalls zu den frühen künstlichen neuronalen Netzen.
								</p>
							</div>
							<div class="flex flex-col gap-4 px-6 pt-4 pb-4 bg-gray-100">
								<div>
									<span
										class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
									>
										NETtalk
									</span>
									<span
										class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
									>
										Neuronale Netze
									</span>
								</div>
								<div>
									<form action="https://de.wikipedia.org/wiki/NETtalk">
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
							<img
								class="w-full"
								src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg"
								alt="Deep Blue"
							/>
							<div class="px-6 py-4 bg-gray-100">
								<div class="font-bold text-2xl mb-2">1997: KI schlägt Schachweltmeister</div>
								<p class="text-gray-700 text-base">
									Die KI "Deep Blue" der Firma IBM, welche für das Schach spielen konzipiert ist,
									bezwingt 1997 den amtierenden Weltmeister Garry Kasparov. Damit ist der bisher von
									Menschen dominierte Bereich des Schachs von einer KI übernommen worden. Dieser
									historische Erfolg wird nur leicht von Kritikern getrübt, die einwerfen, dass
									"Deep Blue" nicht durch kognitive Intelligenz, sondern durch das Berechnen aller
									möglichen Züge gewonnen habe.
								</p>
							</div>
							<div class="flex flex-col gap-4 px-6 pt-4 pb-4 bg-gray-100">
								<div>
									<span
										class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
									>
										Deep Blue
									</span>
									<span
										class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
									>
										KI im Schach
									</span>
								</div>
								<div>
									<form action="https://de.wikipedia.org/wiki/Deep_Blue">
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
							<img
								class="w-full"
								src="https://www.tanikal.com/wp-content/uploads/2016/12/IBM-Logo-Wallpaper-HD.jpg"
								alt="IBM"
							/>
							<div class="px-6 py-4 bg-gray-100">
								<div class="font-bold text-2xl mb-2">2011: "Watson" gewinnt Quizshow</div>
								<p class="text-gray-700 text-base">
									Das Computerprogramm "Watson" tritt 2011 in einer US-amerikanischen TV-Quizshow
									gegen menschliche Mitspieler an und gewinnt die Show. Damit beweist die KI, dass
									sie tatsächlich die natürliche Sprache versteht und eine schnellere
									Reaktionsgeschwindigkeit als die Mitspieler hat.
								</p>
							</div>
							<div class="flex flex-col gap-4 px-6 pt-4 pb-4 bg-gray-100">
								<div>
									<span
										class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
									>
										Watson
									</span>
									<span
										class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
									>
										IBM
									</span>
								</div>
								<div>
									<form action="https://de.wikipedia.org/wiki/Watson_(K%C3%BCnstliche_Intelligenz)">
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
							<img
								class="w-full"
								src="https://medsolut.com/wp-content/uploads/2021/05/20210506_MedSolut_AI_Daily-Life_Blog-Article.jpeg"
								alt="KI im Alltag"
							/>
							<div class="px-6 py-4 bg-gray-100">
								<div class="font-bold text-2xl mb-2">2011-Heute: KI erreicht den Alltag</div>
								<p class="text-gray-700 text-base">
									In den letzten zehn Jahren haben die Wissenschaft und die Technikbranche enorme
									Fortschritte im Bereich der KI gemacht. Diese bahnbrechenden Entwicklungen haben
									der KI den Weg in den Alltag gebahnt: ob bei Google, in den sozialen Medien, Siri,
									Cortana oder Alexa - überall tritt sie auf. Gesamte Unternehmen und private
									Haushalte sind mittlerweile über KI-gesteuerte Systeme vernetzt und kommunizieren
									miteinander, ohne dass die Endverbraucher davon etwas mitbekommen.
								</p>
							</div>
							<div class="flex flex-col gap-4 px-6 pt-4 pb-4 bg-gray-100">
								<div>
									<span
										class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
									>
										KI im Alltag
									</span>
									<span
										class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
									>
										Sprachassistenten
									</span>
								</div>
								<div>
									<form action="https://mixed.de/ki-im-alltag/">
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
							<img
								class="w-full"
								src="https://www.verlagederzukunft.de/wp-content/uploads/2018/12/KI_Algemein_VdZ.jpg"
								alt="KI der Zukunft"
							/>
							<div class="px-6 py-4 bg-gray-100">
								<div class="font-bold text-2xl mb-2">20xx: Die KI der Zukunft</div>
								<p class="text-gray-700 text-base">
									Trotz der bahnbrechenden Entwicklung des vergangenen Jahrzehnts steckt die
									Forschung der KI noch in ihren Anfängen. Das Ziel der Zukunft wird es sein, KI
									zuverlässiger und sicherer in Bereichen wie dem autonomen Fahren, der Raumfahrt
									und besonders in der Medizin zu gestalten. Bisher ist es außerdem nicht gelungen,
									eine sogenannte "starke KI" zu schaffen, die ihr Wissen auf sehr viele Bereiche
									übertragen und somit uns Menschen in jeder Hinsicht übertrumpfen kann. All das
									birgt auch Gefahren, weshalb ethische Fragen zur Forschung und Entwicklung der KI
									immer mehr in der Vordergrund rücken. Die primäre Frage ist und bleibt dabei
									<span class="font-bold">"KI - Fluch oder Segen für den Menschen?"</span>
								</p>
							</div>
							<div class="flex flex-col gap-4 px-6 pt-4 pb-4 bg-gray-100">
								<div>
									<span
										class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
									>
										Starke KI
									</span>
									<span
										class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
									>
										Ethik & Moral
									</span>
								</div>
								<div>
									<form
										action="https://www.kaigondlach.de/artikel/wie-wird-kuenstliche-intelligenz-die-zukunft-veraendern/"
									>
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
			3. Die Arten von KI
		</h1>

		<div class="flex flex-col w-full gap-y-60 items-center">
			<InformationTile
				title="Schwache KI"
				content="Ein KI-System, das nur für die Ausführung einer bestimmten Aufgabe entwickelt und trainiert wurde.
						Es benötigt meist zusätzliche menschliche Intervention und kann ihr Wissen nicht auf andere Bereiche ausweiten.
						Beispiele aus dem Alltag sind Sprachassistenten wie Siri und Alexa oder Industrieroboter."
				class="mt-20"
			>
				<div slot="right_slot">
					<AnimationContainer from_right>
						<img src="../../../static/siri.jpg" alt="vikus_viewer" class="rounded-3xl shadow-2xl" />
					</AnimationContainer>
				</div>
			</InformationTile>
			<InformationTile title="Starke KI" right_side class="mt-20">
				<div slot="content" class="text-gray-400 text-2xl text-justify">
					Auch bekannt als allgemeine künstliche Intelligenz kann die starke KI die kognitiven
					Fähigkeiten des menschlichen Gehirns nachbilden. Somit kann sie auch unbekannte Aufgaben
					lösen, indem sie Wissen aus anderen Bereichen anwendet und selbstständig eine Lösung
					findet. Diese Art von KI ist jedoch nur ein theoretisches Modell, welches es so bisher
					nicht gibt.
				</div>
				<div slot="right_slot">
					<AnimationContainer>
						<img
							src="../../../static/Starke_KI.webp"
							alt="vikus_viewer"
							class="rounded-3xl shadow-2xl"
						/>
					</AnimationContainer>
				</div>
			</InformationTile>
		</div>

		<section class="mb-32 mx-6 mt-48 text-gray-100 text-center bg-gray-800 rounded-2xl p-6">
			<div class="flex justify-center">
				<div class="text-center w-1/2">
					<h2 class="text-6xl font-bold mb-6 text-center">4 Typen von KI</h2>
					<p class="text-2xl text-gray-400 mb-12">
						In <a
							class="text-blue-500 underline"
							href="https://www.govtech.com/computing/understanding-the-four-types-of-artificial-intelligence.html"
							>diesem Artikel</a
						>
						erklärte Arend Hintze, ein Assistenzprofessor für integrative Biologie, Computerwissenschaft
						und Ingenieurwesen an der Michigan State University, dass KI in vier Arten unterteilt werden
						kann. Die vier Kategorien sind:
					</p>
				</div>
			</div>

			<div
				class="grid bg-gray-700 rounded-2xl shadow-2xl p-6 md:grid-cols-2 lg:grid-cols-4 lg:gap-x-12"
			>
				<div class="mb-12 lg:mb-0">
					<div class="p-4 bg-blue-600 rounded-full shadow-lg inline-block mb-6">
						<Icon icon="tablet" size="24px" />
					</div>
					<h5 class="text-2xl font-bold mb-4">1. Reaktive Maschinen (reactive machines)</h5>
					<p class="text-xl text-justify text-gray-300">
						Diese KI-Systeme besitzen keinen eigenen Speicher, aus dem sie Erfahrungen schöpfen
						können, womit sie auch nur einem bestimmten Zweck dienen und aufgabenspezifisch sind.
						Ein Beispiel dafür ist das vorhin aufgeführte, von IBM entwickelte Schachprogramm Deep
						Blue. Dieses System kann Figuren auf dem Schachbrett erkennen und Vorhersagen treffen,
						jedoch aber nicht aus früheren Erkenntnissen lernen.
					</p>
				</div>

				<div class="mb-12 lg:mb-0">
					<div class="p-4 bg-blue-600 rounded-full shadow-lg inline-block mb-6">
						<Icon icon="slack" size="24px" />
					</div>
					<h5 class="text-2xl font-bold mb-4">2. Begrenzte Speicherkapazität (Limited Memory)</h5>
					<p class="text-xl text-justify text-gray-300">
						Anders als die reaktiven Maschinen verfügen diese KI-System über einen Speicher ("ein
						Gedächtnis"), mit welchem sie auf frühere Erfahrungen zurückgreifen und somit neue
						Kenntnisse ziehen können. Solche Systeme kommen unter anderem in autonomen Fahrzeugen
						zum Einsatz.
					</p>
				</div>

				<div class="mb-12 md:mb-0">
					<div class="p-4 bg-blue-600 rounded-full shadow-lg inline-block mb-6">
						<Icon icon="user" size="24px" />
					</div>
					<h5 class="text-2xl font-bold mb-4">3. Theorie des Geistes (Theory of Mind)</h5>
					<p class="text-xl text-justify text-gray-300">
						Ab diesem Typ beginnt langsam der Übergang zur starken KI, denn solche KIs verfügen über
						soziale Intelligenz und können somit Emotionen verstehen. Diese Art von KI wird in der
						Lage sein, menschliche Absichten zu erkennen und Verhalten vorherzusagen, was es ihr
						leichter machen wird, Bestandteil menschlicher Teams zu werden.
					</p>
				</div>

				<div class="mb-12 md:mb-0">
					<div class="p-4 bg-blue-600 rounded-full shadow-lg inline-block mb-6">
						<Icon icon="users" size="24px" />
					</div>
					<h5 class="text-2xl font-bold mb-4">4. Selbstwahrnehmung</h5>
					<p class="text-xl text-justify text-gray-300">
						Künstliche Intelligenzen von diesem Typ besitzen mindestens eine Intelligenz auf
						menschlichem Niveau und einen Sinn für sich selbst, was Ihnen ein eigenes Bewusstsein
						gibt. Sie verstehen ihren eigenen aktuellen Zustand und können uns Menschen in vielen
						Dingen übertreffen, was auch Gefahren birgt.
					</p>
				</div>
			</div>
		</section>
	</div>

	<div id="part-four" class="mt-32">
		<h1 class="headline text-4xl font-bold mb-12 ml-24 uppercase text-gray-100">
			4. Übersicht der wichtigsten Begriffe
		</h1>

		<div class="flex flex-col justify-center items-center">
			<div class="w-1/2 mb-16">
				<h2 class="headline text-3xl font-bold text-gray-100 mb-4">Machine Learning</h2>
				<p class="text-xl text-gray-200 leading-normal text-justify">
					<a href="./ml" class="text-blue-500 underline">Machine Learning</a> ist aktuell einer der bedeutendsten
					Teilbereiche von KI. Mittels Machine Learning werden Systeme/Applikationen geschaffen, die
					mit Hilfe von Daten lernen, Aufgaben zu erfüllen. Der große Vorteil besteht dabei darin, dass
					Programmierer nicht mehr tausende Zeilen von Code schreiben müssen. Stattdessen sorgen mathematische
					Algorithmen dafür, dass das Programm neue Daten automatisch verarbeiten und aus ihnen lernen
					kann. Im Alltag findet man Machine Learning in vielen verschiedenen Bereichen, wie beispielsweise
					bei Empfehlungssystemen in Online-Shops oder Streaming-Diensten, Social Media Feeds oder in
					autonomen Fahrzeugen.
				</p>
			</div>

			<div class="w-1/2 mb-16">
				<h2 class="headline text-3xl font-bold text-gray-100 mb-4">Künstliche neuronale Netze</h2>
				<p class="text-xl text-gray-200 leading-normal text-justify">
					Das Konzept der künstlichen neuronalen Netze ist sehr stark angelehnt an ein rudimentäres
					Bild des menschlichen Gehirns. Mit einem Algorithmus werden verschiedene Schichten
					verbundener Knotenpunkte (Neuronen) geschaffen, die Informationen untereinander
					austauschen. Dabei gibt es Eingangs- und Ausgangsneuronen, zwischen denen sich mehrere
					Zwischenneuronen befinden. Lernt die KI etwas dazu, verknüpfen sich die Eingangsneuronen
					über die Zwischenneuronen mit den Ausgangsneuronen. Erweist sich eine Neuronenverbindung
					als sehr bedeutsam und führt diese oft zur richtigen Vorhersage, erhöht sich die
					Gewichtung der Informationsverknüpfung und festigt sich dadurch (wie im menschlichen
					Gehirn). Revidiert sich eine Entscheidung, so wird die Gewichtung der Verbindung
					geschwächt und andere Kanten geraten in den Vordergrund. Auf diese Art und Weise kann eine
					KI Entscheidungen immer wieder hinterfragen und so lernen, um immer besser in dem
					jeweiligen Anwendungsgebiet zu werden.
				</p>
				<div class="flex justify-center items-center">
					<img
						src="https://t3n.de/magazin/wp-content/uploads/2018/11/neuronale-netze-grafik-620x268.png"
						alt="Neuronales Netz"
						class="rounded-lg my-8"
					/>
				</div>
			</div>

			<div class="w-1/2 mb-16">
				<h2 class="headline text-3xl font-bold text-gray-100 mb-4">Machine Learning</h2>
				<p class="text-xl text-gray-200 leading-normal text-justify">
					<a href="./ml" class="text-blue-500 underline">Machine Learning</a> ist aktuell einer der bedeutendsten
					Teilbereiche von KI. Mittels Machine Learning werden Systeme/Applikationen geschaffen, die
					mit Hilfe von Daten lernen, Aufgaben zu erfüllen. Der große Vorteil besteht dabei darin, dass
					Programmierer nicht mehr tausende Zeilen von Code schreiben müssen. Stattdessen sorgen mathematische
					Algorithmen dafür, dass das Programm neue Daten automatisch verarbeiten und aus ihnen lernen
					kann. Im Alltag findet man Machine Learning in vielen verschiedenen Bereichen, wie beispielsweise
					bei Empfehlungssystemen in Online-Shops oder Streaming-Diensten, Social Media Feeds oder in
					autonomen Fahrzeugen.
				</p>
			</div>
		</div>
	</div>

	<div
		class="flex gap-16 w-full place-self-center items-center justify-center bg-gray-100 shadow-lg"
	>
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
					src="https://mdbcdn.b-cdn.net/img/new/avatars/8.webp"
					class="rounded-full w-32 mb-4 mx-auto"
					alt="Avatar"
				/>
				<h5 class="text-xl font-medium leading-tight mb-2">Robert Witzke</h5>
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

<style lang="postcss">
</style>
