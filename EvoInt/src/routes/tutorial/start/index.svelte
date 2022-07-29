<script lang="ts">
	import Header from '../../../components/Header.svelte';
	import AnimationContainer from '../../../components/AnimationContainer.svelte';
	import Footer from '../../../components/Footer.svelte';
	import TutorialTextArea from '../../../components/TutorialTextArea.svelte';
</script>

<Header />

<div class="flex flex-col text-center justify-center items-center mt-20">
	<div
		class="mb-56 headline text-center text-base  sm:text-lg md:text-xl lg:text-3xl xl:text-5xl 2xl:text-6xl font-bold uppercase text-gray-100 [text-shadow:0_4px_8px_rgba(255,255,255,0.25)]"
	>
		Wie funktioniert der EvoInt-Tracker?
	</div>

	<AnimationContainer>
		<p
			class="headline text-base  sm:text-lg md:text-xl lg:text-3xl xl:text-5xl 2xl:text-6xl font-bold uppercase text-gray-100 [text-shadow:0_4px_8px_rgba(255,255,255,0.25)]"
		>
			Was ist EvoInt?
		</p>
	</AnimationContainer>

	<TutorialTextArea icon="help-circle" icon_size="32px" icon_color="#000000">
		<div
			slot="content"
			class="text-gray-700 text-justify text-base sm:text-lg md:text-xl lg:text-2xl"
		>
			EvoInt ist ein Tracker zur interaktiven Visualisierung der historischen Entwicklung von
			Intelligenz- und anderen Fachbegriffen in wissenschaftlichen Publikationen. Machine Learning
			sowie verwandte Themen wie 
			<span
				class="text-base  sm:text-lg md:text-xl lg:text-2xl font-mono"
			>
				Künstliche Intelligenzen, Natural Language Processing
			</span>
			sind mittlerweile etablierte Themengebiete der Informatik, die viel Aufmerksamkeit genießen. Jedoch
			gibt es bisher keine Studien zur historischen Entwicklung des Auftretens dieser und weiteren dazugehörigen
			Fachbegriffen in wissenschaftlichen Publikationen. Mit
			<bold class="font-bold">EvoInt</bold> wollen wir diesen Umstand verbessern. Über den Vikus-Viewer
			und die analysierten Daten der IJCAI und ECAI ist es nun möglich, exakt diese historische Entwicklung zu
			sehen und auf einen Blick nachzuvollziehen.
		</div>
	</TutorialTextArea>

	<AnimationContainer>
		<p
			class="headline text-base  sm:text-lg md:text-xl lg:text-3xl xl:text-5xl 2xl:text-6xl font-bold uppercase text-gray-100 [text-shadow:0_4px_8px_rgba(255,255,255,0.25)]"
		>
			Wie funktioniert es?
		</p>
	</AnimationContainer>

	<TutorialTextArea icon="list" icon_size="32px" icon_color="#000000">
		<div
			slot="content"
			class="text-gray-700 text-justify text-base sm:text-lg md:text-xl lg:text-2xl"
		>
			Der Vikus-Viewer ist sowohl über die Startseite als auch über die Tutorial-Seite erreichbar.
			In der animierten Darstellung befinden sich, nach Jahren unterteilt, alle Paper der IJCAI und ECAI, in
			denen Wörter passend zum Thema Machine Learning und Künstliche Intelligenz auftauchen. Am
			oberen Bildschirmrand befindet sich eine Liste von Wörtern, nach denen in den Publikationen
			gesucht wird. Dabei ist es möglich, einzelne Wörter anzuklicken und speziell nach diesen zu
			filtern, sodass nur noch Paper mit den ausgewählten Begriffen dargestellt werden. Außerdem
			kann man mithilfe des Mausrads auf die einzelnen Paper zoomen und einige Informationen, wie
			beispielsweise den Autor, das Erstellungsdatum und die Quelle, sowie eine Vorschau des Papers
			erhalten.
		</div>
	</TutorialTextArea>

	<AnimationContainer>
		<p
			class="headline text-base  sm:text-lg md:text-xl lg:text-3xl xl:text-5xl 2xl:text-6xl font-bold uppercase text-gray-100 [text-shadow:0_4px_8px_rgba(255,255,255,0.25)]"
		>
			Wie wird analysiert?
		</p>
	</AnimationContainer>

	<TutorialTextArea icon="activity" icon_size="32px" icon_color="#000000">
		<div
			slot="content"
			class="text-gray-700 text-justify text-base sm:text-lg md:text-xl lg:text-2xl"
		>
			Bisher werden die Datensätze aller Publikationen der IJCAI und ECAI ausschließlich anhand der
			Worthäufigkeit analysiert. Das heißt, dass bislang keine semantische Analyse vorgenommen wird.
			Jedoch entkräftigt die fehlende Semantik die Aussage der Datenanalyse nur eingeschränkt.
			Aspekte wie eine zunehmende Entwicklung hinsichtlich der Anzahl von Papers sowie die sich
			ändernden auftretenden Wörtern in den Texten, sind dennoch erkennbar. Trotzdem ist es
			zukünftig geplant, 
			<span
				class="text-base  sm:text-lg md:text-xl lg:text-2xl font-mono"
			>
				Natural Language Processing
			</span>
			zu integrieren, um auch semantische Aspekte der Textanalyse mitaufzunehmen und die Analyse noch
			wertvoller zu machen.
		</div>
	</TutorialTextArea>
</div>

<Footer />

<style lang="postcss">

</style>
