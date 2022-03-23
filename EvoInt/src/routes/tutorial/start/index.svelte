<script lang="ts">
	import Header from '../../../components/Header.svelte';
    import AnimationContainer from '../../../components/AnimationContainer.svelte';
	import Footer from '../../../components/Footer.svelte';
</script>

<Header />

<div class="flex flex-col text-center justify-center items-center mt-20">
	<h1
		class="mb-20 text-6xl font-bold uppercase text-gray-100 [text-shadow:0_4px_8px_rgba(255,255,255,0.25)]"
	>
		Wie funktioniert der EvoInt-Tracker?
	</h1>
</div>

<div class="flex">
	<div class="pt-36 w-1/3 flex flex-col items-center">
		<div class="h-[90vh]">
			<AnimationContainer>
				<h2>Was</h2>
			</AnimationContainer>

			<AnimationContainer delay="0.1s">
				<h2 class="ml-28">ist</h2>
			</AnimationContainer>

			<AnimationContainer delay="0.2s">
				<h2 class="ml-52">EvoInt?</h2>
			</AnimationContainer>
		</div>
		<div class="h-[90vh]">
			<AnimationContainer>
				<h2>Wie</h2>
			</AnimationContainer>

			<AnimationContainer delay="0.1s">
				<h2 class="ml-28">funktioniert</h2>
			</AnimationContainer>

			<AnimationContainer delay="0.2s">
				<h2 class="ml-52">es?</h2>
			</AnimationContainer>
		</div>
		<div class="h-[90vh]">
			<AnimationContainer>
				<h2>Wie</h2>
			</AnimationContainer>

			<AnimationContainer delay="0.1s">
				<h2 class="ml-28">wird</h2>
			</AnimationContainer>

			<AnimationContainer delay="0.2s">
				<h2 class="ml-52">analysiert?</h2>
			</AnimationContainer>
		</div>
	</div>
	<div
		class="w-2/3 p-10 pt-36 border-l-2 border-l-gray-800 flex flex-col justify-center items-center"
	>
		<div class="w-3/4 h-[90vh] flex flex-col gap-5">
			<p>EvoInt ist ein Tracker zur interaktiven Visualisierung der historischen Entwicklung von Intelligenz- und anderen Fachbegriffen in wissenschaftlichen Publikationen.</p>
            <hr>
			<p class="text-justify">
				Machine Learning sowie verwandte Themen wie <span class="text-xl font-mono"
					>Künstliche Intelligenzen, Natural Language Processing</span
				>
				sind mittlerweile etablierte Themengebiete der Informatik, die viel Aufmerksamkeit genießen.
                Jedoch gibt es bisher keine Studien zur historischen Entwicklung des Auftretens dieser und weiteren dazugehörigen Fachbegriffen in wissenschaftlichen Publikationen.
				Mit <bold class="font-bold">EvoInt</bold> wollen wir diesen Umstand verbessern. Über den Vikus-Viewer und die analysierten Daten der IJCAI ist es nun möglich,
                exakt diese historische Entwicklung zu sehen und auf einen Blick nachzuvollziehen.
			</p>
		</div>
		<div class="w-3/4 h-[90vh] flex flex-col gap-5">
			<p>
                Der Vikus-Viewer ist sowohl über die Startseite als auch über die Tutorial-Seite erreichbar. In der animierten Darstellung befinden sich, nach Jahren unterteilt, alle Paper der IJCAI, in denen
                Wörter passend zum Thema Machine Learning und Künstliche Intelligenz auftauchen. Am oberen Bildschirmrand befindet sich eine Liste von Wörtern, nach denen in den Publikationen gesucht wird.
                Dabei ist es möglich, einzelne Wörter anzuklicken und speziell nach diesen zu filtern, sodass nur noch Paper mit den ausgewählten Begriffen dargestellt werden. Außerdem kann man mithilfe des
                Mausrads auf die einzelnen Paper zoomen und einige Informationen, wie beispielsweise den Autor, das Erstellungsdatum und die Quelle, sowie eine Vorschau des Papers erhalten.
			</p>
		</div>
		<div class="w-3/4 h-[90vh] flex flex-col gap-5">
			<p>
                Bisher werden die Datensätze aller Publikationen der IJCAI ausschließlich anhand der Worthäufigkeit analysiert. Das heißt, dass bislang keine semantische Analyse vorgenommen wird.
                Jedoch entkräftigt die fehlende Semantik die Aussage der Datenanalyse nur eingeschränkt. Aspekte wie eine zunehmende Entwicklung hinsichtlich der Anzahl von Papers sowie die
                sich ändernden auftretenden Wörtern in den Texten, sind dennoch erkennbar. Trotzdem ist es zukünftig geplant, <span class="text-xl font-mono">Natural Language Processing</span>
                zu integrieren, um auch semantische Aspekte der Textanalyse mitaufzunehmen und die Analyse noch wertvoller zu machen.
                <!-- Bei NLP Link zur eigenen NLP Info-Page -->
			</p>
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
		@apply text-2xl text-gray-400;
	}
</style>