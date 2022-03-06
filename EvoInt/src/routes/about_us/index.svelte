<script lang="ts">
	import Header from '../../components/Header.svelte';
	import AnimationContainer from '../../components/AnimationContainer.svelte';
	import Icon from '../../components/Icon.svelte';
	import TeamMemberCard from './_TeamMemberCard.svelte';
</script>

<Header />

<div class="flex">
	<div class="pt-36 w-1/2 flex flex-col items-center">
		<div class="h-[90vh]">
			<AnimationContainer>
				<h1>Wer</h1>
			</AnimationContainer>

			<AnimationContainer delay="0.1s">
				<h1 class="ml-28">wir</h1>
			</AnimationContainer>

			<AnimationContainer delay="0.2s">
				<h1 class="ml-52">sind.</h1>
			</AnimationContainer>
		</div>
		<div class="h-[90vh]">
			<AnimationContainer>
				<h1>Unsere</h1>
			</AnimationContainer>

			<AnimationContainer delay="0.1s">
				<h1 class="ml-28">Hochschule:</h1>
			</AnimationContainer>

			<AnimationContainer delay="0.2s">
				<h1 class="ml-52">Die HWR</h1>
			</AnimationContainer>
		</div>
		<div class="h-[90vh]">
			<AnimationContainer>
				<h1>A</h1>
			</AnimationContainer>

			<AnimationContainer delay="0.1s">
				<h1 class="ml-28">B</h1>
			</AnimationContainer>

			<AnimationContainer delay="0.2s">
				<h1 class="ml-52">C</h1>
			</AnimationContainer>
		</div>
		<div class="h-[90vh]">
			<AnimationContainer>
				<h1>D</h1>
			</AnimationContainer>

			<AnimationContainer delay="0.1s">
				<h1 class="ml-28">E</h1>
			</AnimationContainer>

			<AnimationContainer delay="0.2s">
				<h1 class="ml-52">F</h1>
			</AnimationContainer>
		</div>
	</div>
	<div
		class="w-1/2 p-10 pt-36 border-l-2 border-l-gray-800 flex flex-col justify-center items-center"
	>
		<div class="w-2/3 h-[90vh] flex flex-col gap-5">
			<p>Wir sind ein Team aus vier Studenten.</p>
			<div class="self-center flex flex-col gap-2">
				<div class="flex gap-2">
					<TeamMemberCard
						icons={['code', 'layout']}
						name="Denis Knecht"
						description="Entwickler, Design, Backend"
					/>
					<TeamMemberCard
						icons={['code', 'layout']}
						name="Robert Witzke"
						description="Entwickler, Design, Backend"
					/>
				</div>
				<div class="flex gap-2">
					<TeamMemberCard
						icons={['code', 'layout']}
						name="Marten Kaffler"
						description="Entwickler, Design, Backend"
					/>
					<TeamMemberCard
						icons={['code', 'layout']}
						name="Hamid"
						description="Entwickler, Design, Backend"
					/>
				</div>
			</div>
			<p class="text-justify">
				Zum Zeitpunkt der Fertigstellung dieser Webseite <span class="text-xl font-mono"
					>(August 2022)</span
				>
				absolvieren wir das vierte Semester im Bereich Informatik in Form eines dualen Studiums an der
				<bold class="font-bold">HWR</bold>
				<span class="text-xl font-mono">(Hochschule für Wirtschaft und Recht)</span>. Weitere
				Informationen zur HWR befinden sich weiter unten auf dieser Seite.
			</p>
		</div>
		<div class="w-2/3 h-[90vh] flex flex-col gap-5">
			<div class="p-2 bg-white rounded-md shadow-sm shadow-white">
				<img src="HWR.png" alt="HWR Logo" />
			</div>
			<p>
				Ad aliqua commodo ad velit culpa ullamco. Est exercitation in cupidatat consectetur sit
				culpa occaecat. Incididunt aliqua voluptate exercitation reprehenderit excepteur commodo
				fugiat. Pariatur eu dolor cillum anim. Officia consequat elit est est excepteur deserunt
				exercitation aliqua deserunt esse adipisicing consectetur laboris reprehenderit. Fugiat duis
				ipsum sit qui aute ullamco incididunt est cillum. Proident veniam aliqua culpa nostrud
				deserunt aliquip qui dolor deserunt culpa.
			</p>
		</div>
		<div class="h-[90vh]">
			<p>
				Ad aliqua commodo ad velit culpa ullamco. Est exercitation in cupidatat consectetur sit
				culpa occaecat. Incididunt aliqua voluptate exercitation reprehenderit excepteur commodo
				fugiat. Pariatur eu dolor cillum anim. Officia consequat elit est est excepteur deserunt
				exercitation aliqua deserunt esse adipisicing consectetur laboris reprehenderit. Fugiat duis
				ipsum sit qui aute ullamco incididunt est cillum. Proident veniam aliqua culpa nostrud
				deserunt aliquip qui dolor deserunt culpa.
			</p>
		</div>
		<div class="h-[90vh]">
			<p>
				Ad aliqua commodo ad velit culpa ullamco. Est exercitation in cupidatat consectetur sit
				culpa occaecat. Incididunt aliqua voluptate exercitation reprehenderit excepteur commodo
				fugiat. Pariatur eu dolor cillum anim. Officia consequat elit est est excepteur deserunt
				exercitation aliqua deserunt esse adipisicing consectetur laboris reprehenderit. Fugiat duis
				ipsum sit qui aute ullamco incididunt est cillum. Proident veniam aliqua culpa nostrud
				deserunt aliquip qui dolor deserunt culpa.
			</p>
		</div>
	</div>
</div>

<style lang="postcss">
	h1 {
		@apply text-8xl font-bold uppercase text-gray-100 [text-shadow:0_4px_8px_rgba(255,255,255,0.25)] select-none;
	}
	p {
		@apply text-2xl text-gray-400;
	}
	li {
		@apply flex items-center gap-2;
	}
	li > p {
		@apply text-white font-bold;
	}
</style>
