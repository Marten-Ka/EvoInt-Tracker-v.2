<script lang="ts">
	import Header from '../../components/Header.svelte';
	import AnimationContainer from '../../components/AnimationContainer.svelte';
	import Footer from '../../components/Footer.svelte';
</script>

<Header />

<div class="flex flex-col text-center justify-center items-center mt-20">
	<AnimationContainer>
		<div
			class="headline text-center text-base  sm:text- md:text-xl lg:text-3xl xl:text-5xl 2xl:text-6xl font-bold uppercase text-gray-100 [text-shadow:0_4px_8px_rgba(255,255,255,0.25)] select-none"
		>
			Wer wir sind.
		</div>
	</AnimationContainer>

	<section
		class="p-8 max-w-4xl xl:max-w-6xl 2xl:max-w-7xl text-gray-800 text-center bg-gray-800 rounded-xl mt-12 mb-80"
	>
		<div class="grid gap-x-6 lg:gap-x-12 md:grid-cols-4 mt-16">
			<div class="mb-24 md:mb-0">
				<div class="rounded-lg shadow-lg h-full block bg-white">
					<div class="flex justify-center">
						<div class="flex justify-center" style="margin-top: -75px">
							<img
								src="/Robert.jfif"
								class="rounded-full mx-auto shadow-lg"
								alt=""
								style="width: 150px"
							/>
						</div>
					</div>
					<div class="p-6">
						<h5 class="text-lg font-bold mb-4">Robert Witzke</h5>
						<p class="mb-6">Frontend Developer</p>
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

			<div class="mb-24 md:mb-0">
				<div class="rounded-lg shadow-lg h-full block bg-white">
					<div class="flex justify-center">
						<div class="flex justify-center" style="margin-top: -75px">
							<img
								src="https://static.smplf.io/wordpress/uploads/sites/12/nerd.jpeg"
								class="rounded-full mx-auto shadow-lg"
								alt=""
								style="width: 150px"
							/>
						</div>
					</div>
					<div class="p-6">
						<h5 class="text-lg font-bold mb-4">Denis Knecht</h5>
						<p class="mb-6">Backend Developer</p>
						<ul class="list-inside flex mx-auto justify-center">
							<a href="https://github.com/DenisKnecht02" class="px-2">
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
						</ul>
					</div>
				</div>
			</div>

			<div class="mb-24 md:mb-0">
				<div class="rounded-lg shadow-lg h-full block bg-white">
					<div class="flex justify-center">
						<div class="flex justify-center" style="margin-top: -75px">
							<img
								src="/Marten.jfif"
								class="rounded-full mx-auto shadow-lg"
								alt=""
								style="width: 150px"
							/>
						</div>
					</div>
					<div class="p-6">
						<h5 class="text-lg font-bold mb-4">Marten Kaffler</h5>
						<p class="mb-6">Frontend Developer</p>
						<ul class="list-inside flex mx-auto justify-center">
							<a href="https://github.com/Marten-Ka" class="px-2">
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
							<a href="https://www.linkedin.com/in/marten-kaffler-33aa85211" class="px-2">
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

			<div class="">
				<div class="rounded-lg shadow-lg h-full block bg-white">
					<div class="flex justify-center">
						<div class="flex justify-center" style="margin-top: -75px">
							<img
								src="/Hamid.jfif"
								class="rounded-full mx-auto shadow-lg"
								alt=""
								style="width: 150px"
							/>
						</div>
					</div>
					<div class="p-6">
						<h5 class="text-lg font-bold mb-4">Hamid Omar</h5>
						<p class="mb-6">Web Designer</p>
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

		<p class="text-xl text-justify m-8 text-gray-300">
			Wir sind ein Team aus vier Studenten. Zum Zeitpunkt der Fertigstellung dieser Webseite <span
				class="text-xl font-mono">(August 2022)</span
			>
			absolvieren wir das vierte Semester im Bereich Informatik in Form eines dualen Studiums an der
			<bold class="font-bold">HWR</bold>
			<span class="text-xl font-mono">(Hochschule für Wirtschaft und Recht)</span>. Weitere
			Informationen zur HWR befinden sich weiter unten auf dieser Seite.
		</p>
	</section>

	<AnimationContainer>
		<div
			class="headline text-center text-base  sm:text- md:text-xl lg:text-3xl xl:text-5xl 2xl:text-6xl font-bold uppercase text-gray-100 [text-shadow:0_4px_8px_rgba(255,255,255,0.25)] select-none"
		>
			Unsere Hochschule: Die HWR
		</div>
	</AnimationContainer>

	<div class="max-w-4xl xl:max-w-6xl 2xl:max-w-7xl mt-12 mb-80">
		<div class="block rounded-lg shadow-lg bg-gray-800 m-4">
			<div class="flex flex-col lg:grid lg:grid-cols-3">
				<div
					class="w-full flex p-6 justify-center bg-white items-center rounded-t-lg lg:rounded-t-none lg:rounded-l-lg mb-6 lg:mb-0 mx-auto md:mx-0"
				>
					<img src="/HWR.png" alt="HWR Logo" />
				</div>
				<div class="px-6 place-self-center col-span-2 py-8">
					<p class="text-gray-300 text-xl text-justify mb-6">
						Zu dem dualen Studiengang Informatik an der HWR Berlin gehört im vierten Semester die
						Bearbeitung eines Studienprojektes von einem mehrköpfigen Team von Studenten. Die Arbeit
						an der Webseite sowie die Implementierung und Erweiterung des Vikus-Viewers finden im
						Rahmen dieses Projektes statt. An unserem Thema zur Entwicklung des Begriffs der
						Künstlichen Intelligenz, bzw. EvoInt, wurde schon in den Vorjahren gearbeitet. Dabei
						haben vorangegangene Studenten Daten von der IJCAI analysiert und ausgewertet sowie in
						den Vikus-Viewer integriert, jedoch konnte man diese Ergebnisse bisher nicht einsehen.
						Mit unserer von der HWR gehosteten Webseite ändert sich das, denn nun ist es möglich,
						die Ergebnisse öffentlich aufzurufen und interaktiv zu nutzen sowie sich einen Überblick
						zum Thema mithilfe der informativen Seiten zu verschaffen. Das Thema der dazugehörigen
						Studienarbeit lautet "Weiterentwicklung eines Trackers zur interaktiven Visualisierung
						der historischen Entwicklung von Intelligenz- und anderen Fachbegriffen in
						wissenschaftlichen Publikationen.".
					</p>
				</div>
			</div>
		</div>
	</div>
</div>

<Footer />

<style lang="postcss">
</style>
