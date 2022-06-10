<script lang="ts">
	import TutorialRedirectButton from '../../../components/_TutorialRedirectButton.svelte';
	import AnimationContainer from '../../../components/AnimationContainer.svelte';
	import Footer from '../../../components/Footer.svelte';
	import Header from '../../../components/Header.svelte';

	const redirects = [
		{ text: '1. Der Begriff der Künstlichen Intelligenz', href: '#part-one', icon: 'terminal' },
		{ text: '2. Die historische Entwicklung von KI', href: '#part-two', icon: 'terminal' },
		{ text: '3. Die Arten von KI', href: '#part-three', icon: 'terminal' }
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

<div class="flex flex-col m-6 mt-32">
	<div id="part-one">
		<h1
			class="headline text-4xl font-bold mb-12 ml-24 uppercase text-gray-100 [text-shadow:0_4px_8px_rgba(255,255,255,0.5)]"
		>
			1. Der Begriff der Künstlichen Intelligenz
		</h1>

		<!-- <div class="flex justify-center">
			<div class="flex flex-col md:flex-row md:max-w-xl rounded-lg bg-white shadow-lg">
				<div class="w-full text-center m-6">
					<img
						src="https://mdbcdn.b-cdn.net/img/new/avatars/8.webp"
						class="rounded-full w-32 mb-4 mx-auto"
						alt="Avatar"
					/>
					<h5 class="text-xl font-medium leading-tight mb-2">John Doe</h5>
					<p class="text-gray-500">Web designer</p>
				</div>
				<div class="p-6 flex flex-col justify-start">
					<h5 class="text-gray-900 text-xl font-medium mb-2">Card title</h5>
					<p class="text-gray-700 text-base mb-4">
						This is a wider card with supporting text below as a natural lead-in to additional
						content. This content is a little bit longer.
					</p>
					<p class="text-gray-600 text-xs">Last updated 3 mins ago</p>
				</div>
			</div>
		</div> -->

		<section
			class="flex flex-col place-content-start gap-16 my-16 p-16 text-center md:text-left shadow-lg rounded-md bg-cover"
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
								<p class="text-gray-500 text-lg font-semibold italic mb-6">
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
								<p class="text-gray-500 text-lg font-semibold italic mb-6">
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
								<p class="text-gray-500 text-lg font-semibold italic mb-6">
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

	<div id="part-two">
		<h1
			class="headline text-4xl font-bold mb-12 ml-24 uppercase text-gray-100 [text-shadow:0_4px_8px_rgba(255,255,255,0.5)]"
		>
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
											class="inline-block px-4 py-1.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded-full shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
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

	<div id="part-three">
		<h1
			class="headline text-4xl font-bold mb-12 ml-24 uppercase text-gray-100 [text-shadow:0_4px_8px_rgba(255,255,255,0.5)]"
		>
			3. Die Arten von KI
		</h1>
	</div>
</div>

<Footer />

<style lang="postcss">
</style>
