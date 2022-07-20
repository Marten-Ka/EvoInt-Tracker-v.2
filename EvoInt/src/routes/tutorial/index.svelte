<script lang="ts">
	import Header from '../../components/Header.svelte';
	import AnimationContainer from '../../components/AnimationContainer.svelte';
	import TutorialRedirectButton from '../../components/_TutorialRedirectButton.svelte';
	import Footer from '../../components/Footer.svelte';

	const redirects = [
		{ text: 'Wie funktioniert der EvoInt-Tracker?', href: 'tutorial/start', icon: 'help-circle' },
		{ text: 'Künstliche Intelligenz', href: 'tutorial/ki', icon: 'cpu' },
		{ text: 'Machine Learning', href: 'tutorial/ml', icon: 'book-open' },
		{ text: 'Natural Language Processing', href: 'tutorial/nlp', icon: 'message-square' }
	];
</script>

<Header />

<div class="flex flex-col w-full group-w-auto text-center justify-center items-center mt-20 mb-96 ">
	<h1
		class="mb-20 font-bold uppercase text-gray-100 text-sm  sm:text-lg md:text-xl lg:text-3xl xl:text-5xl xl:text-4xl 2xl:text-6xl [text-shadow:0_4px_8px_rgba(255,255,255,0.25)]"
	>
		Willkommen zum Tutorial <br /> zur künstlichen Intelligenz
	</h1>

	<div class="flex flex-col gap-10 sm:gap-4 md:gap-6 lg:gap-8 ">
		{#each redirects as redirect, i}
			<AnimationContainer delay={i <= 5 ? String(i * 0.5) + 's' : '0s'}>
				<TutorialRedirectButton text={redirect.text} href={redirect.href} icon={redirect.icon} />
			</AnimationContainer>
		{/each}
	</div>
  <div id="part-one" class="mt-32">
		<section
			class="flex flex-col place-content-start gap-16 mx-6 my-16 p-16 text-center md:text-left shadow-lg rounded-md bg-cover"
			style="background-image: url(https://mdbcdn.b-cdn.net/img/Photos/Others/background2.jpg)"
		>
			<div class="flex justify-start">
				<div class="max-w-4xl xl:max-w-6xl 2xl:max-w-7xl">
					<div class="block p-6 rounded-lg shadow-lg bg-white m-4">
						<div class="md:flex md:flex-row">
							<div class="md:ml-6 place-self-center">
								<p class="text-gray-500 text-xl font-semibold italic mb-6  text-center">
									Here comes explanation about tutorial dfgadff adfasdfasdfas fdasfasdfasdfasdf asdffasdfasdfasdfasfasdf asdfasdfasdfasdfasdfasfdsa 
								</p>
							</div>
						</div>
					</div>
				</div>
			</div>
		</section>
	</div>
</div>


<Footer />

<style lang="postcss">
</style>
