<script lang="ts">
	import Header from '../../components/Header.svelte';
	import AnimationContainer from '../../components/AnimationContainer.svelte';
	import TutorialRedirectButton from './_TutorialRedirectButton.svelte';
</script>

<Header />

<div class="flex flex-col text-center justify-center items-center mt-20">
	<h1
		class="mb-20 text-6xl font-bold uppercase text-gray-100 [text-shadow:0_4px_8px_rgba(255,255,255,0.25)]"
	>
		Willkommen zum Tutorial <br /> zur künstlichen Intelligenz
	</h1>

	<div>
		<AnimationContainer>
			<TutorialRedirectButton text="Vikus Viewer" href="tutorial/vikus_viewer" icon="search" />
		</AnimationContainer>
		<AnimationContainer delay="0.5s">
			<TutorialRedirectButton text="Künstliche Intelligenz" href="tutorial/ki" icon="cpu" />
		</AnimationContainer>
		<AnimationContainer delay="1s">
			<TutorialRedirectButton text="Machine Learning" href="tutorial/ki" icon="book-open" />
		</AnimationContainer>
		<AnimationContainer delay="1.5s">
			<TutorialRedirectButton text="Wie fange ich an?" href="tutorial/ki" icon="help-circle" />
		</AnimationContainer>
	</div>
</div>

<style lang="postcss">
</style>
