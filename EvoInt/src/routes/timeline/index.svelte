<script lang="ts">
	import TimelineCard from '../../components/TimelineCard.svelte';
	import Footer from '../../components/Footer.svelte';
	import Header from '../../components/Header.svelte';
</script>

<Header />

<div class="p-10 flex justify-center">
	<div class=" flex flex-col items-center content-around gap-40 w-4 py-14 bg-gray-900 rounded-3xl">
		<div class="white bg-white font-mono text-2xl rounded-lg p-4">Start</div>

		<TimelineCard
			position="flex-col-reverse"
			date="19.01.2022"
			heading="Bekanntgabe des Studienprojektes"
			content="Am 19.01. fand die erste Besprechung zu allgemeinen Informationen und Abläufen des Studienprojekts statt,
			in der ebenfalls Meetings für genauere Diskussionen zu den einzelnen Themen ausgemacht wurden."
		/>

		<TimelineCard
			position="flex-col"
			date="20.01.2022"
			heading="Aufgabenbesprechung"
			content="In einem ausführlicheren Meeting mit der betreuenden Professorin wurde besprochen, wie das schon begonnene
			Studienprojekt erweitert werden könnte und welche Aufgaben anstehen."
		/>

		<TimelineCard
			position="flex-col-reverse"
			date="01.02.2022"
			heading="Einarbeitung"
			content="Zu Beginn beschäftigten sich alle Teammitglieder mit dem ersten Stand des Projektes und der dazugehörigen
			Studienarbeit über den Download und die Analyse der wissenschaftlichen Publikationen. Zudem wurde das Projekt
			zum ersten Mal ausgeführt und sich ein Überblick über den Code verschafft."
		/>

		<TimelineCard
			position="flex-col"
			date="17.02.2022"
			heading="VIKUS-Viewer"
			content="In einem Meeting mit dem zweiten Projektteam stellte dieses den VIKUS-Viewer vor, mit welchem die Ergebnisse
			des ersten Projektteams visualisiert wurden."
		/>

		<TimelineCard
			position="flex-col-reverse"
			date="20.02.2022"
			heading="Gruppeneinteilung"
			content="Für die Erstellung dieser Webseite wurden hauptsächlich Robert Witzke und Hamid Omar verantwortlich gemacht.
			Denis Knecht sollte sich um das Code-Refactoring kümmern und Marten Kaffler an der semantischen Analyse der Texte
			mit NLP forschen."
		/>

		<TimelineCard
			position="flex-col"
			date="24.03.2022"
			heading="Projektpräsentation"
			content="Am 24.03.2022 wurde der bisherige Bearbeitungsstand des Projektes an der Hochschule vorgestellt."
		/>

		<TimelineCard
			position="flex-col-reverse"
			date="11.06.2022"
			heading="Code-Refactoring"
			content="Die Optimierung und das Aufräumen des Codes wurde am 01.06. fertiggestellt, womit der Download und die Analyse
			der Papers nun deutlich nutzerfreundlicher und effektiver sind."
		/>

		<TimelineCard
			position="flex-col"
			date="26.07.2022"
			heading="Webseite"
			content="Am 26.07. wurde die Webseite fertiggestellt, die nun gehostet werden sollte."
		/>

		<TimelineCard
			position="flex-col-reverse"
			date="11.08.2022"
			heading="Hosting"
			content="Nachdem die HWR einen Server zur Verfügung gestellt hatte, konnte die Webseite erfolgreich auf diesem gehostet werden.
			Der Zugriff geschieht über das private Netzwerk der Hochschule."
		/>

		<TimelineCard
			position="flex-col"
			date="19.08.2022"
			heading="NLP"
			content="Der inhaltliche Vergleich der wissenschaftlichen Fachliteraturen mithilfe von NLP wurde fertiggestellt. Die
			Ergebnisse dessen sind verschiedene Grafiken und Matrizen, die die Ähnlichkeit verschiedener Papers visualisieren."
		/>

		<TimelineCard
			position="flex-col-reverse"
			date="23.08.2022"
			heading="Abgabe der Studienarbeit"
			content="Am 23.08.2022 fand die Abgabe der finalen Version der Studienarbeit statt, die einige Tage zuvor beendet wurde."
		/>
	</div>
</div>

<Footer />

<style lang="postcss">
</style>
