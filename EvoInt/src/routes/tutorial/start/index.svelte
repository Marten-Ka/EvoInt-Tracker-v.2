<script lang="ts">
	import Header from '../../../components/Header.svelte';
	import AnimationContainer from '../../../components/AnimationContainer.svelte';
	import Footer from '../../../components/Footer.svelte';
	import Icon from '../../../components/Icon.svelte';
</script>

<Header />

<div class="flex flex-col text-center justify-center items-center mt-20">
	<div
		class="mb-56 headline text-center text-base  sm:text-lg md:text-xl lg:text-3xl xl:text-5xl xl:text-4xl 2xl:text-6xl font-bold uppercase text-gray-100 [text-shadow:0_4px_8px_rgba(255,255,255,0.25)]"
	>
		Wie funktioniert der EvoInt-Tracker?
</div>

	<AnimationContainer>
		<p class="headline text-base  sm:text-lg md:text-xl lg:text-3xl xl:text-5xl xl:text-4xl 2xl:text-6xl font-bold uppercase text-gray-100 [text-shadow:0_4px_8px_rgba(255,255,255,0.25)]">Was ist <span class="text-sky-500">EvoInt</span>?</p>
	</AnimationContainer>

	<div class="max-w-4xl xl:max-w-6xl 2xl:max-w-7xl mt-12 mb-80">
		<div class="block p-8 pr-12 rounded-lg shadow-lg bg-white m-4">
			<div class="md:flex md:flex-row">
				<div
					class="md:w-96 w-36 flex flex-col gap-4 mt-1 items-center mb-6 lg:mb-0 mx-auto md:mx-0"
				>
					<Icon icon="help-circle" size="32px" color="#000000" />
				</div>
				<div class="md:ml-6 place-self-center">
					<p class="text-gray-700 text-base  sm:text-lg md:text-xl lg:text-2xl">
						EvoInt ist ein Tracker zur interaktiven Visualisierung der historischen Entwicklung
						von Intelligenz- und anderen Fachbegriffen in wissenschaftlichen Publikationen.
						Machine Learning sowie verwandte Themen wie <span class="text-base  sm:text-lg md:text-xl lg:text-2xl font-mono"
							>Künstliche Intelligenzen, Natural Language Processing</span
						>
						sind mittlerweile etablierte Themengebiete der Informatik, die viel Aufmerksamkeit genießen.
						Jedoch gibt es bisher keine Studien zur historischen Entwicklung des Auftretens dieser
						und weiteren dazugehörigen Fachbegriffen in wissenschaftlichen Publikationen. Mit
						<bold class="font-bold">EvoInt</bold> wollen wir diesen Umstand verbessern. Über den
						Vikus-Viewer und die analysierten Daten der IJCAI ist es nun möglich, exakt diese historische
						Entwicklung zu sehen und auf einen Blick nachzuvollziehen.
					</p>
				</div>
			</div>
		</div>
	</div>

	<AnimationContainer>
		<p class="headline text-base  sm:text-lg md:text-xl lg:text-3xl xl:text-5xl xl:text-4xl 2xl:text-6xl font-bold uppercase text-gray-100 [text-shadow:0_4px_8px_rgba(255,255,255,0.25)]">Wie funktioniert es?</p>
	</AnimationContainer>

	<div class="max-w-4xl xl:max-w-6xl 2xl:max-w-7xl mt-12 mb-80">
		<div class="block p-8 pr-12 rounded-lg shadow-lg bg-white m-4">
			<div class="md:flex md:flex-row">
				<div
					class="md:w-96 w-36 flex flex-col gap-4 mt-1 items-center mb-6 lg:mb-0 mx-auto md:mx-0"
				>
					<Icon icon="list" size="32px" color="#000000" />
				</div>
				<div class="md:ml-6 place-self-center">
					<p class="text-gray-700 text-base  sm:text-lg md:text-xl lg:text-2xl">
						Der Vikus-Viewer ist sowohl über die Startseite als auch über die Tutorial-Seite
						erreichbar. In der animierten Darstellung befinden sich, nach Jahren unterteilt,
						alle Paper der IJCAI, in denen Wörter passend zum Thema Machine Learning und
						Künstliche Intelligenz auftauchen. Am oberen Bildschirmrand befindet sich eine Liste
						von Wörtern, nach denen in den Publikationen gesucht wird. Dabei ist es möglich,
						einzelne Wörter anzuklicken und speziell nach diesen zu filtern, sodass nur noch
						Paper mit den ausgewählten Begriffen dargestellt werden. Außerdem kann man mithilfe
						des Mausrads auf die einzelnen Paper zoomen und einige Informationen, wie
						beispielsweise den Autor, das Erstellungsdatum und die Quelle, sowie eine Vorschau
						des Papers erhalten.
					</p>
				</div>
			</div>
		</div>
	</div>

	<AnimationContainer>
		<p class="headline text-base  sm:text-lg md:text-xl lg:text-3xl xl:text-5xl xl:text-4xl 2xl:text-6xl font-bold uppercase text-gray-100 [text-shadow:0_4px_8px_rgba(255,255,255,0.25)]">Wie wird analysiert?</p>
	</AnimationContainer>

	<div class="max-w-4xl xl:max-w-6xl 2xl:max-w-7xl mt-12 mb-80">
		<div class="block p-8 pr-12 rounded-lg shadow-lg bg-white m-4">
			<div class="md:flex md:flex-row">
				<div
					class="md:w-96 w-36 flex flex-col gap-4 mt-1 items-center mb-6 lg:mb-0 mx-auto md:mx-0"
				>
					<Icon icon="activity" size="32px" color="#000000" />
				</div>
				<div class="md:ml-6 place-self-center">
					<p class="text-gray-700 text-base  sm:text-lg md:text-xl lg:text-2xl">
						Bisher werden die Datensätze aller Publikationen der IJCAI ausschließlich anhand der
						Worthäufigkeit analysiert. Das heißt, dass bislang keine semantische Analyse
						vorgenommen wird. Jedoch entkräftigt die fehlende Semantik die Aussage der
						Datenanalyse nur eingeschränkt. Aspekte wie eine zunehmende Entwicklung hinsichtlich
						der Anzahl von Papers sowie die sich ändernden auftretenden Wörtern in den Texten,
						sind dennoch erkennbar. Trotzdem ist es zukünftig geplant, <span
							class="text-base  sm:text-lg md:text-xl lg:text-2xl font-mono">Natural Language Processing</span>
						zu integrieren, um auch semantische Aspekte der Textanalyse mitaufzunehmen und die Analyse
						noch wertvoller zu machen.
					</p>
				</div>
			</div>
		</div>
	</div>

</div>

<Footer />

<style lang="postcss">
	h1 {
		@apply text-8xl font-bold uppercase text-gray-100 [text-shadow:0_4px_8px_rgba(255,255,255,0.25)] select-none;
	}
	h2 {
		@apply text-6xl font-bold uppercase text-gray-100 [text-shadow:0_4px_8px_rgba(255,255,255,0.25)] select-none;
	}
	p {
		@apply text-justify;
	}
</style>
